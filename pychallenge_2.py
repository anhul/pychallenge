"""Python challenge number 2."""
#!/usr/local/bin/python3
from collections import Counter

import requests
from bs4 import BeautifulSoup, Comment
import pychallenge_common

CHALL_LINK = "http://www.pythonchallenge.com/pc/def/ocr.html"

def get_rare_characters(text, rate=1):
    """
    Count character occurrence.

    Count character occurrence in the text and return characters which
    occur less or equal times than rate value.
    """
    chars_rate = Counter(text)

    return [char for char, count in chars_rate.items() if count <= rate]


def execute():
    """Run main function."""
    challenge_page_link = CHALL_LINK
    raw_html = pychallenge_common.get_page_content(challenge_page_link)

    if raw_html:
        commented_text = pychallenge_common.get_text_in_comments(raw_html)
        rare_chars = get_rare_characters(commented_text[1])
        next_challenge = pychallenge_common.get_next_challenge("".join(rare_chars))

        return next_challenge

    return None


if __name__ == "__main__":
    print(execute())
