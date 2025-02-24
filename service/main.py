from datetime import datetime, timezone

from fastapi import FastAPI, HTTPException, Response, status
from models.metadata import Metadata
from models.model import RMRModel
from models.schemas import HealthStatus, InputData, OutputData
from otel import setup_telemetry, meter, logger

start_time_utc = datetime.now(timezone.utc)  # Store the time the api starts

rmr_model = RMRModel()


app = FastAPI(
    title=Metadata.title,
    description=Metadata.description,
    version=Metadata.version,
    contact=Metadata.contact,
    license_info=Metadata.license_info,
    openapi_tags=Metadata.tags,
)

setup_telemetry(app)

@app.get("/", tags=["Root"])
async def root():
    logger.info("Root endpoint called")
    
    return {
        "message": (
            "Welcome to the RMR API. Use /docs for the API" + " documentation."
        )
    }


@app.post("/rmr/", tags=["RMR"], response_model=OutputData)
async def calculate_rmr(input_data: InputData, response: Response):
    """
    Endpoint to calculate RMR over a time projection using Mifflin-St. Jeor
    equations.
    """
    logger.info("RMR calculation endpoint called with input data: %s", input_data)
    
    result = rmr_model.process(input_data.model_dump())

    if result["exit_code"] != 0:
        logger.error("RMR calculation failed with error: %s", result["error"])
        raise HTTPException(status_code=422, detail=result["error"])
    logger.info("RMR calculation successful with result: %s", result)
    
    response.status_code = status.HTTP_200_OK
    
    return {
        "sex": result["sex"],
        "units": result["units"],
        "age": result["age"],
        "weight": result["weight"],
        "height": result["height"],
        "weight_loss_rate": result["weight_loss_rate"],
        "duration": result["duration"],
        "rmr": result["rmr"],
        "time_projection": result["time_projection"],
    }


@app.get("/health", tags=["Health"], response_model=HealthStatus)
async def health_check(response: Response):
    logger.info("Health check endpoint called")
    
    current_time_utc = datetime.now(timezone.utc)
    uptime_utc = current_time_utc - start_time_utc
    
    response.status_code = status.HTTP_200_OK
    
    health_status = {
        "status": "healty",
        "uptime_utc": str(uptime_utc),
        "timestamp": str(current_time_utc.isoformat()),
    }
    logger.info("Health check status: %s", health_status)
    
    return health_status
