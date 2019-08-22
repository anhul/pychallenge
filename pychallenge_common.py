"""Common functions used in python challenges"""

import requests
from bs4 import BeautifulSoup, Comment

OK_STATUS_CODE = 200
CHALL_LINK_PATTERN = "http://www.pythonchallenge.com/pc/def/{keyword}.html"


def get_page_content(url, params=None):
    """Try to get the contents of the html web page."""
    try:
        resp = requests.get(url, params=params)
        if is_response_ok(resp):
            return resp.text

        return None

    except requests.exceptions.RequestException:
        return None


def get_text_in_comments(html_content):
    """Retrieve text from html comment tags: <!-- text -->."""
    soup = BeautifulSoup(html_content, features="html.parser")
    comments_list = soup.findAll(text=lambda text: isinstance(text, Comment))

    return comments_list


def get_next_challenge(keyword):
    """Return link to the next challenge."""
    chall_link_pattern = CHALL_LINK_PATTERN

    return chall_link_pattern.format(keyword=keyword)


def is_response_ok(resp):
    r"""
    Verify if a response is successful.

    Verify if response onto GET request is successful and Content-Type header
    field is text\html.
    """
    content_type = resp.headers["Content-Type"].lower()

    return (resp.status_code == OK_STATUS_CODE
            and content_type is not None
            and content_type.find("html") > -1)
