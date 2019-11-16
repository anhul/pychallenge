"""Common functions used in python challenges"""

import os
import requests
from bs4 import BeautifulSoup, Comment
from configs import configure_logger

OK_STATUS_CODE = 200
CH_URL_PATTERN = "http://www.pythonchallenge.com/pc/def/{keyword}.html"

logger = configure_logger(__name__)

def get_page_content(url, params=None):
    """Get the content of the web page."""
    try:
        resp = requests.get(url, params=params)
        if is_response_ok(resp):
            return resp.text

        return None

    except requests.exceptions.RequestException:
        return None

def download_file(url, filename=None):
    """Download file from the url and save in the location specified by filename"""
    try:
        resp = requests.get(url)
        if is_response_ok(resp):
            if filename is None:
                filename = os.path.basename(url)
            with open(filename, "wb") as f:
                f.write(resp.content)
            return filename
        return None
    except requests.exceptions.RequestException:
        return None


def is_response_ok(resp):
    r"""
    Verify if a response is successful.

    Verify if response onto GET request is successful and Content-Type header
    field is not empty.
    """
    content_type = resp.headers["Content-Type"]
    logger.debug("Response status code: {}".format(resp.status_code))
    logger.debug("Response content type: {}".format(content_type))
    return (resp.status_code == OK_STATUS_CODE
            and content_type is not None)


def get_text_in_comments(html_content):
    """Retrieve text from html comment tags: <!-- text -->."""
    soup = BeautifulSoup(html_content, features="html.parser")
    comments_list = soup.findAll(text=lambda text: isinstance(text, Comment))

    return comments_list


def get_next_challenge(keyword):
    """
    Return url to the next challenge.

    Compose url to the next challenge basing on the keyword.
    Check if the url is reachable. Follow redirects if applicable
    """
    ch_url_pattern = CH_URL_PATTERN
    url = ch_url_pattern.format(keyword=keyword)
    try:
        logger.debug("Connecting to {} ...".format(url))
        resp = requests.get(url, allow_redirects=False)
        if not is_response_ok(resp):
            return None
        # Check for meta refresh redirects
        refresh_url = get_meta_refresh_url(resp.text)
        if refresh_url:
            url = replace_file(resp.url, refresh_url)
            logger.debug("Redirecting to {} ...".format(url))
            resp = requests.get(url, allow_redirects=False)
            if not is_response_ok(resp):
                return None
    except requests.exceptions.ConnectionError:
        logger.debug("Internet connection is not available")
        return None

    return resp.url


def get_meta_refresh_url(page_html):
    """Retrieve URL from meta refresh"""
    soup = BeautifulSoup(page_html, "html.parser")
    meta = soup.find("meta", attrs={"http-equiv":"Refresh"})
    if meta:
        content_url = meta["content"].split(";")[1]
        if content_url.strip().lower().startswith("url="):
            url = content_url.strip()[4:]
            return url

    return None


def url_response_ok(url):
    """Check whether url is reachable"""
    try:
        logger.debug("Connecting to {} ...".format(url))
        resp = requests.get(url)
        logger.debug("Response status code: {}".format(resp.status_code))
    except requests.exceptions.ConnectionError:
        logger.debug("Internet connection is not available")
        return False

    return resp.status_code == OK_STATUS_CODE


def replace_file_ext(file_path, new_ext):
    """Replace file extension."""
    file_name, _ = os.path.splitext(file_path)

    return f"{file_name}.{new_ext}"

def replace_file(file_path, new_file):
    """Replace file in the file path."""
    file_dir = os.path.dirname(file_path)

    return os.path.join(file_dir, new_file)

if __name__ == "__main__":
    ok_url = "http://www.pythonchallenge.com/pc/def/274877906944.html"
    notok_url = "http://www.pythonchallenge.com/pc/def/opr.html"
    get_next_challenge("274877906944")
