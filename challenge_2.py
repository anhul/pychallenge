"""Solution for challenge number 2."""

from collections import Counter
from configs import configure_logger
from utils import common

CH_URL = "http://www.pythonchallenge.com/pc/def/ocr.html"
logger = configure_logger(__name__)

def get_rare_characters(text, rate=1):
    """
    Count character occurrence.

    Count character occurrence in the text and return characters which
    occur less or equal times than rate value.
    """
    chars_rate = Counter(text)
    return [char for char, count in chars_rate.items() if count <= rate]


def execute():
    """Start challenge execution."""
    ch_url = CH_URL
    html_content = common.get_page_content(ch_url)
    if html_content is None:
        return None

    commented_text = common.get_text_in_comments(html_content)
    rare_chars = get_rare_characters(commented_text[1])
    next_ch_url = common.get_next_challenge("".join(rare_chars))
    if not common.url_response_ok(next_ch_url):
        return None

    return next_ch_url


if __name__ == "__main__":
    execute()
