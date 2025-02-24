from . import otel_metrics
from opentelemetry.instrumentation.logging import LoggingInstrumentor

meter = otel_metrics.meter


try:
    from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor # type: ignore
    instrumentator = FastAPIInstrumentor()
    log_message = "FastAPI instrumentator initialized"
except:
    from opentelemetry.instrumentation.flask import FlaskInstrumentor # type: ignore
    instrumentator = FlaskInstrumentor()
    log_message = "Flask instrumentator initialized"


def setup_telemetry(app) -> None:
    """Sets up OpenTelemetry instrumentation for FastAPI."""

    # Instrument FastAPI
    instrumentator.instrument_app(app)
