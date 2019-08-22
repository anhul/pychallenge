"""Python challenge number 2."""
#!/usr/local/bin/python3
from collections import Counter

import requests
from bs4 import BeautifulSoup, Comment


OK_STATUS_CODE = 200

CHALL_LINK = "http://www.pythonchallenge.com/pc/def/ocr.html"
CHALL_LINK_PATTERN = "http://www.pythonchallenge.com/pc/def/{keyword}.html"


def get_page_content(url):
    """Try to get the contents of the html web page."""
    try:
        resp = requests.get(url)
        if is_response_ok(resp):
            return resp.content

        return None

    except requests.exceptions.RequestException:
        return None


def get_text_in_comments(html_content):
    """Retrieve text from html comment tags: <!-- text -->."""
    soup = BeautifulSoup(html_content, features="html.parser")
    comments_list = soup.findAll(text=lambda text: isinstance(text, Comment))

    return comments_list


def get_rare_characters(text, rate=1):
    """
    Count character occurrence.

    Count character occurrence in the text and return characters which
    occur less or equal times than rate value.
    """
    chars_rate = Counter(text)

    return [char for char, count in chars_rate.items() if count <= rate]


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


def main():
    """Run main function."""
    challenge_page_link = CHALL_LINK
    raw_html = get_page_content(challenge_page_link)

    if raw_html:
        commented_text = get_text_in_comments(raw_html)
        rare_chars = get_rare_characters(commented_text[1])

        return get_next_challenge("".join(rare_chars))

    return None


if __name__ == "__main__":
    main()
