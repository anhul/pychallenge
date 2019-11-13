import os
import logging
import datetime

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

LOG_DIR = os.path.join(ROOT_DIR, "logs")
LOG_LEVEL = logging.DEBUG
LOGGER_NAME = "executor"

def configure_logger(name, level=LOG_LEVEL):
    """Configure logger with file and stream handlers"""
    # Get logger instance identified by the name
    logger = logging.getLogger(name)
    # Set logging level for the logger
    logger.setLevel(level)

    # Create log directory if not exists
    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)
    # Create log name format basing on the date and time of the execution
    log_name = name + datetime.datetime.now().strftime("%Y%m%d_%H%M%S") + ".log"

    # Create file handler
    fh = logging.FileHandler(os.path.join(LOG_DIR, log_name))
    fh.setLevel(level)
    # create console handler
    ch = logging.StreamHandler()
    ch.setLevel(level)

    # create formatter and add it to the handlers
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(module)s- %(levelname)s - %(lineno)d - %(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)

    # add the handlers to the logger
    logger.addHandler(fh)
    logger.addHandler(ch)

    return logger