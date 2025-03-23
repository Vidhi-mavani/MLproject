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

# Main code
if __name__ == "__main__":
    try:
        a = 1 / 0  # This will raise a ZeroDivisionError
    except Exception as e:
        logging.info("Divide by zero")  # Log the error
        raise CustomException("A custom error occurred", sys) from e  # Raise the custom exception
