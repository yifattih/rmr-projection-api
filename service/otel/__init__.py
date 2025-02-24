from . import otel_metrics, otel_logs
from opentelemetry.instrumentation.logging import LoggingInstrumentor

meter = otel_metrics.meter
logger = otel_logs.logger


try:
    from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor # type: ignore
    instrumentator = FastAPIInstrumentor()
    instrumentator_name = "FastAPI"
except:
    from opentelemetry.instrumentation.flask import FlaskInstrumentor # type: ignore
    instrumentator = FlaskInstrumentor()
    instrumentator_name = "Flask"
finally:
    logger.info(f"{instrumentator_name} instrumentator found and initialized")

def setup_telemetry(app) -> None:
    """Sets up OpenTelemetry instrumentation for FastAPI."""
    logger.info("Starting OpenTelemetry configuration setup")

    # Instrument
    instrumentator.instrument_app(app)
    logger.info(f"{instrumentator_name} instrumentator created")

    # Instrument Python standard logging
    LoggingInstrumentor().instrument(
        set_logging_format=True,
        logging_format="%(asctime)s %(levelname)s %(name)s %(filename)s:%(lineno)d %(otelTraceID)s %(otelSpanID)s %(message)s",
    )
    logger.info("Logging instrumentator initialized")

    logger.info("OpenTelemetry configuration done")