"""Solution for challenge number 0."""

from configs import configure_logger
from utils import common

CH_NUMBER = 0
CH_URL = "http://www.pythonchallenge.com/pc/def/0.html"
logger = configure_logger(__name__)

def execute():
    """Start challenge execution."""
    logger.info("Challenge {}, URL {}".format(CH_NUMBER, CH_URL))
    next_ch_url = common.get_next_challenge(str(2**38))
    logger.info("Next challenge {}, URL {}".format(CH_NUMBER+1, next_ch_url))

    return next_ch_url


if __name__ == "__main__":
    execute()
