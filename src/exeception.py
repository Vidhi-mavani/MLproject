import sys
import logging

# Error message formatter function
def error_message_detail(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()  # Corrected typo: exe_info -> exc_info
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occurred in python script name [{0}] line number [{1}] error message[{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )  # Corrected: fixed the typo and added the return statement
    return error_message  # Fixed the typo for return

# Custom Exception class (with correct name)
class CustomException(Exception):  # Fixed typo: "Excepton" -> "Exception"
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)  # Corrected the super() call
        self.error_message = error_message_detail(error_message, error_detail)  # Fixed argument passing

    def __str__(self):
        return self.error_message  # Fixed indentation

# Set up logging configuration
LOG_FILE = "logfile.log"
logging.basicConfig(
    filename=LOG_FILE,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(message)s",
    level=logging.INFO
)


