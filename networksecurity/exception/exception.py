import sys

from networksecurity.logging.logger import logger


class NetworkSecurityException(Exception):
    """
    Custom Exception Class for the Network Security Project.
    Stores useful debugging information such as
    file name, line number, and error message.
    """

    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)

        # Extract traceback information
        _, _, exc_tb = error_detail.exc_info()

        self.file_name = exc_tb.tb_frame.f_code.co_filename
        self.line_number = exc_tb.tb_lineno
        self.error_message = error_message

    def __str__(self):
        return (
            f"Error occurred in Python script "
            f"[{self.file_name}] "
            f"at line [{self.line_number}] "
            f"with message: {self.error_message}"
        )


# ---------------------------------------------------
# Testing Logging and Exception Handling
# ---------------------------------------------------

if __name__ == "__main__":

    try:
        logger.info("Entered the try block.")

        # Generate an exception intentionally
        result = 1 / 0

    except Exception as e:

        logger.error("An exception has occurred.")

        raise NetworkSecurityException(e, sys)