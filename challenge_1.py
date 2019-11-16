"""Solution for challenge number 1."""

import os
from bs4 import BeautifulSoup
from configs import configure_logger
from utils import common

CH_NUMBER = 1
CH_URL = "http://www.pythonchallenge.com/pc/def/map.html"
logger = configure_logger(__name__)

def retrieve_encoded_message(html_text):
    """
    Retrieve encoded message from the HTML.
    """
    soup = BeautifulSoup(html_text, "html.parser")
    font = soup.find("font", attrs={"color":"#f000f0"})

    return font.get_text()


def decode_message(message, shift_right=2):
    """Decode text message"""
    z_code = 122
    a_before_code = 96
    decoded_list = []
    for symbol in message:
        if symbol.isalpha():
            shifted_code = ord(symbol) + shift_right
            if z_code - shifted_code >= 0:
                new_symbol = chr(shifted_code)
            else:
                new_symbol = chr(a_before_code + shifted_code - z_code)
        else:
            new_symbol = symbol
        decoded_list.append(new_symbol)

    return "".join(decoded_list)


def execute():
    """Start challenge execution."""
    logger.info("Challenge {}, URL {}".format(CH_NUMBER, CH_URL))
    ch_url = CH_URL
    html_content = common.get_page_content(ch_url)
    if html_content is None:
        return None
    message = retrieve_encoded_message(html_content)
    logger.debug("Encoded text from page: {}".format(message))
    decoded_message = decode_message(message)
    logger.debug("Decoded text from page: {}".format(decoded_message))
    ch_url_file_name, _ = os.path.splitext(os.path.basename(ch_url))
    next_ch_url = common.get_next_challenge(decode_message(ch_url_file_name))
    logger.info("Next challenge {}, URL {}".format(CH_NUMBER+1, next_ch_url))

    return next_ch_url


if __name__ == "__main__":
    execute()
