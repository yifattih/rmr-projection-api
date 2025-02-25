from opentelemetry.instrumentation.logging import LoggingInstrumentor

from . import otel_logs, otel_metrics, otel_traces

meter = otel_metrics.meter
logger = otel_logs.logger
tracer = otel_traces.tracer

try:  # pragma: no cover
    from opentelemetry.instrumentation.fastapi import (
        FastAPIInstrumentor,
    )  # type: ignore

    instrumentator = FastAPIInstrumentor()
    instrumentator_name = "FastAPI"
except ImportError:  # pragma: no cover
    from opentelemetry.instrumentation.flask import (
        FlaskInstrumentor,
    )  # type: ignore

    instrumentator = FlaskInstrumentor()
    instrumentator_name = "Flask"
finally:  # pragma: no cover
    logger.info(f"{instrumentator_name} instrumentator found and initialized")  # type: ignore


def setup_telemetry(app) -> None:  # pragma: no cover
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
    logger.info("Logging instrumentator created")

    logger.info("OpenTelemetry configuration done")
