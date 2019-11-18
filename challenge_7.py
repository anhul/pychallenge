"""Solution for challenge number 7."""

from configs import configure_logger
from utils import common
from bs4 import BeautifulSoup
from PIL import Image
import numpy as np

CH_NUMBER = 7
CH_URL = "http://www.pythonchallenge.com/pc/def/oxygen.html"
logger = configure_logger(__name__)

def retrieve_image_url(html_content):
    """
    Retrieve url to the image to be processed.
    """
    soup = BeautifulSoup(html_content, "html.parser")
    center = soup.find("center")
    img_scr = center.img["src"]
    url = common.replace_file(CH_URL, img_scr)

    return url


def process_image(filepath):
    """Process image, find encrypted message and decode it"""
    image = Image.open(filepath)
    width, height = image.size
    band = image.getbands()
    logger.debug("Image width: {}. Image height: {}".format(width, height))
    logger.debug("Image band: {}".format(band))
    # Get pixels tuples
    pixels = list(image.getdata())
    # Create rows of pixels
    pixels = [pixels[i * width:(i + 1) * width] for i in range(height)]
    encrypted_row = pixels[height//2]
    logger.debug("One row with encrypted pixels: {}".format(encrypted_row))

    pixel_temp = (0, 0, 0, 0)
    char_codes = []
    for pixel in encrypted_row:
        if pixel != pixel_temp:
            r, g, b, _ = pixel
            if r == g == b:
                char_codes.append(r)
        pixel_temp = pixel
    logger.debug("Characters codes retrieved from pixels: {}".format(char_codes))
    decoded_message = "".join(map(chr, char_codes))
    logger.debug("Decoded message: {}".format(decoded_message))

    open_br_index = decoded_message.index("[")
    close_br_index = decoded_message.index("]")
    str_codes = decoded_message[open_br_index + 1: close_br_index].split(", ")
    keyword_chars = [chr(int(code)) for code in str_codes]
    logger.debug("Decoded keyword characters: {}".format(keyword_chars))
    keyword = "".join(keyword_chars)
    trans_dict = {"\n":"n", "\x10":"t", "\x0e":"r"}
    trans_table = keyword.maketrans(trans_dict)
    keyword = keyword.translate(trans_table)

    return keyword


def execute():
    """Start challenge execution."""
    logger.info("Challenge {}, URL {}".format(CH_NUMBER, CH_URL))
    ch_url = CH_URL
    html_content = common.get_page_content(ch_url)
    if html_content is None:
        return None
    img_url = retrieve_image_url(html_content)
    filepath = common.download_file(img_url)
    keyword = process_image(filepath)
    next_ch_url = common.get_next_challenge(keyword)
    logger.info("Next challenge {}, URL {}".format(CH_NUMBER+1, next_ch_url))

    return next_ch_url


if __name__ == "__main__":
    execute()
