from loguru import logger

logger.add(
    "C:\\Workspace\\MKL\\MKL\\project\\log\\logging.log",
    rotation='2MB',
    compression="zip",
    format="{time:YYYY-MM-DD-HH:mm:ss} || {level} || {message}",
    level="INFO"
)
