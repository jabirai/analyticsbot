import logging
import os


def setup_logger(log_file_path):
    # Extract directory from the log file path
    log_directory = os.path.dirname(log_file_path)

    # Check if the directory exists, and if not, create it
    if not os.path.exists(log_directory):
        os.makedirs(log_directory, exist_ok=True)

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    # Create handlers
    f_handler = logging.FileHandler(log_file_path, mode="w")
    f_handler.setLevel(logging.INFO)

    # Add handlers to the logger
    logger.addHandler(f_handler)

    return logger
