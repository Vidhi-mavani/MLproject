import sys
import logging
from exeception import CustomException  # Import CustomException

# Set up logging configuration
LOG_FILE = "logfile.log"
logging.basicConfig(
    filename=LOG_FILE,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(message)s",
    level=logging.INFO
)

