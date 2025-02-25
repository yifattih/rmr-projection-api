from datetime import datetime, timezone

from fastapi import FastAPI, HTTPException, Response, status
from models.metadata import Metadata
from models.model import RMRModel
from models.schemas import HealthStatus, InputData, OutputData
from otel import logger, meter, setup_telemetry, tracer

service_start_time_utc = datetime.now(timezone.utc)

service = FastAPI(
    title=Metadata.title,
    description=Metadata.description,
    version=Metadata.version,
    contact=Metadata.contact,
    license_info=Metadata.license_info,
    openapi_tags=Metadata.tags,
)

setup_telemetry(service)

with tracer.start_as_current_span("rmr_model_init"):
    start_time = datetime.now(timezone.utc)

    rmr_model = RMRModel()

    end_time = datetime.now(timezone.utc)
    latency = (end_time - start_time).total_seconds()

    meter.create_counter(
        name="rmr_model_initializations",
        description="Counts the number of times the RMR model is initialized",
        unit="initializations",
    ).add(1)

    meter.create_histogram(
        name="rmr_model_initialization_latency",
        description="Measures the latency of RMR model initialization",
        unit="seconds",
    ).record(latency)


@service.get("/", tags=["Root"])
async def root():
    with tracer.start_as_current_span("root_span"):
        logger.info("Root endpoint called")

        meter.create_counter(
            name="root_endpoint_calls",
            description="Counts the number of times the root endpoint is called",
            unit="calls",
        ).add(1)

        start_time = datetime.now(timezone.utc)

        response = {
            "message": (
                "Welcome to the RMR API. Use /docs for the API"
                + " documentation."
            )
        }

        end_time = datetime.now(timezone.utc)
        latency = (end_time - start_time).total_seconds()

        meter.create_histogram(
            name="root_endpoint_latency",
            description="Measures the latency of the root endpoint",
            unit="seconds",
        ).record(latency)

        return response


@service.post("/rmr/", tags=["RMR"], response_model=OutputData)
async def calculate_rmr(input_data: InputData, response: Response):
    """
    Endpoint to calculate RMR over a time projection using Mifflin-St. Jeor
    equations.
    """
    with tracer.start_as_current_span("rmr_span"):
        logger.info(
            "RMR calculation endpoint called with input data: %s", input_data
        )

        meter.create_counter(
            name="rmr_calculation_requests",
            description="Counts the number of RMR calculation requests",
            unit="requests",
        ).add(1)

        start_time = datetime.now(timezone.utc)

        result = rmr_model.process(input_data.model_dump())

        end_time = datetime.now(timezone.utc)
        latency = (end_time - start_time).total_seconds()

        meter.create_histogram(
            name="rmr_calculation_latency",
            description="Measures the latency of RMR calculations",
            unit="seconds",
        ).record(latency)

        if result["exit_code"] != 0:  # pragma: no cover
            logger.error(
                "RMR calculation failed with error: %s", result["error"]
            )
            meter.create_counter(
                name="rmr_calculation_failures",
                description="Counts the number of failed RMR calculations",
                unit="failures",
            ).add(1)
            raise HTTPException(status_code=422, detail=result["error"])

        logger.info("RMR calculation successful with result: %s", result)
        meter.create_counter(
            name="rmr_calculation_successes",
            description="Counts the number of successful RMR calculations",
            unit="successes",
        ).add(1)

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


@service.get("/health", tags=["Health"], response_model=HealthStatus)
async def health_check(response: Response):
    """
    Health check endpoint that returns the status of the service.
    Parameters
    ----------
    response : Response
        The response object data scheme.
    Returns
    -------
    dict
        A dictionary containing the health status, uptime in UTC, and the current timestamp in ISO format.
    Notes
    -----
    This function logs the health check status and sets the response status code to 200 OK.
    """
    with tracer.start_as_current_span("health_span") as span:
        logger.info("Health check endpoint called")

        meter.create_counter(
            name="health_check_requests",
            description="Counts the number of health check requests",
            unit="requests",
        ).add(1)

        start_time = datetime.now(timezone.utc)

        current_time_utc = datetime.now(timezone.utc)
        uptime_utc = current_time_utc - service_start_time_utc

        span.set_attribute("health_check.uptime_utc", str(uptime_utc))

        logger.info("Service uptime UTC: %s", uptime_utc)

        response.status_code = status.HTTP_200_OK

        health_status = {
            "status": "healthy",
            "uptime_utc": str(uptime_utc),
            "timestamp": str(current_time_utc.isoformat()),
        }
        logger.info("Health check status: %s", health_status)

        end_time = datetime.now(timezone.utc)
        latency = (end_time - start_time).total_seconds()

        meter.create_histogram(
            name="health_check_latency",
            description="Measures the latency of health check requests",
            unit="seconds",
        ).record(latency)

        meter.create_counter(
            name="health_check_successes",
            description="Counts the number of successful health checks",
            unit="successes",
        ).add(1)

        # Measure service uptime
        meter.create_histogram(
            name="service_uptime",
            description="Measures the service uptime in seconds",
            unit="seconds",
        ).record(uptime_utc.total_seconds())

        return health_status
