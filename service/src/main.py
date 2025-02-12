from fastapi import FastAPI, HTTPException
from prometheus_fastapi_instrumentator import Instrumentator

from .models.model import RMRModel
from .schemas import InputData, RMROutput

app = FastAPI(
    title="Resting Metabolic Rate (RMR) API",
    description=(
        "A RESTful API for calculating RMR using Mifflin-St. Jeor"
        + " equations."
    ),
    version="1.0.0",
)

rmr_model = RMRModel()


@app.get("/", tags=["Root"])
async def root():
    return {
        "message": (
            "Welcome to the RMR API. Use /docs for the API" + " documentation."
        )
    }


@app.post("/rmr/", response_model=RMROutput)
async def calculate_rmr(input_data: InputData):
    """
    Endpoint to calculate RMR over a time projection using Mifflin-St. Jeor
    equations.
    """
    result = rmr_model.process(input_data.model_dump())

    if result["exit_code"] != 0:
        raise HTTPException(status_code=400, detail=result["error"])

    return {"input": result["input"], "output": result["output"]}


# Instrumentation to expose metrics endpoint for Prometheus
Instrumentator().instrument(app).expose(app)
