from datetime import datetime, timezone

from fastapi import FastAPI, HTTPException, Response, status
from prometheus_fastapi_instrumentator import Instrumentator

from .models.model import RMRModel
from .schemas import HealthStatus, InputData, OutputData

rmr_model = RMRModel()
start_time_utc = datetime.now(timezone.utc)  # Store the time the api starts

app = FastAPI(
    title="Resting Metabolic Rate (RMR) API",
    description=(
        "A RESTful API for calculating RMR using Mifflin-St. Jeor"
        + " equations."
    ),
    version="1.0.0",
)


@app.get("/", tags=["Root"])
async def root():
    return {
        "message": (
            "Welcome to the RMR API. Use /docs for the API" + " documentation."
        )
    }


@app.post("/rmr/", response_model=OutputData)
async def calculate_rmr(input_data: InputData, response: Response):
    """
    Endpoint to calculate RMR over a time projection using Mifflin-St. Jeor
    equations.
    """
    result = rmr_model.process(input_data.model_dump())

    if result["exit_code"] != 0:
        raise HTTPException(
            status_code=400,
            detail=result["error"]
            )

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
        "time_projection": result["time_projection"]}


@app.get("/health", response_model=HealthStatus)
async def health_check(response: Response):
    current_time_utc = datetime.now(timezone.utc)
    uptime_utc = current_time_utc - start_time_utc
    response.status_code = status.HTTP_200_OK
    return {
        "status": "healty",
        "uptime_utc": str(uptime_utc),
        "timestamp": str(current_time_utc.isoformat()),
    }


# Instrumentation to expose metrics endpoint for Prometheus
Instrumentator().instrument(app).expose(app)
