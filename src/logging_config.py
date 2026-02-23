import logging


class HealthCheckFilter(logging.Filter):
    """Filter out /health endpoint logs"""

    def filter(self, record: logging.LogRecord) -> bool:
        return "/health" not in record.getMessage()


def setup_logging():
    """Configure logging to filter health checks"""
    # Get uvicorn access logger
    uvicorn_logger = logging.getLogger("uvicorn.access")
    uvicorn_logger.addFilter(HealthCheckFilter())
