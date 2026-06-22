import logging
import os
from datetime import datetime

# Create a unique log file name using the current date and time
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Create the path where log files will be stored
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)

# Create the logs directory if it doesn't already exist
os.makedirs(os.path.dirname(logs_path), exist_ok=True)

# Configure the logging system
logging.basicConfig(
    filename=logs_path,  # Log file location
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,  # Log INFO and above (WARNING, ERROR, CRITICAL)
)

# Create a logger object
logger = logging.getLogger("NetworkSecurityLogger")