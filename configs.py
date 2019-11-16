import os
import logging
import datetime

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

LOG_DIR = os.path.join(ROOT_DIR, "logs")
LOG_LEVEL = logging.DEBUG
LOG_FORMAT = "'%(asctime)s %(name)s %(levelname)s %(module)s:%(lineno)d - %(message)s'"
LOG_NAME_BASE = "pychallenge_"

CH_SRC_TEMP = os.path.join(ROOT_DIR, "utils", "challenge_n.txt")
CH_TEST_TEMP = os.path.join(ROOT_DIR, "utils", "test_challenge_n.txt")

def configure_logger(name, level=LOG_LEVEL):
    """Configure logger with file and stream handlers"""
    # Get logger instance identified by the name
    logger = logging.getLogger(name)
    # Set logging level for the logger
    logger.setLevel(level)

    # Create log formatter
    formatter = logging.Formatter(LOG_FORMAT)

    # Do not log into a file when module is run as a script
    if name != "__main__":
        # Create log directory if not exists
        if not os.path.exists(LOG_DIR):
            os.makedirs(LOG_DIR)

        # Create log name format basing on the date and time of the execution
        log_name = LOG_NAME_BASE + datetime.datetime.now().strftime(
            "%Y%m%d_%H%M%S") + ".log"

        # Create file handler and set formatter to it
        fh = logging.FileHandler(os.path.join(LOG_DIR, log_name))
        fh.setLevel(level)
        fh.setFormatter(formatter)
        # Add file handler to the logger
        logger.addHandler(fh)

    # create console handler and add him to the logger
    ch = logging.StreamHandler()
    ch.setLevel(level)
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    return logger