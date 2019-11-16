"""Python challenge number 5."""
import os
import pickle
from bs4 import BeautifulSoup
from utils import common

CHALL_URL = "http://www.pythonchallenge.com/pc/def/peak.html"

def get_hidden_keyword(page_text):
    """Retreive the hidden keyword from the html page"""
    soup = BeautifulSoup(page_text, features="html.parser")
    peakhell = soup.find("peakhell")

    return peakhell["src"]


def get_next_url(url, new_url_ending):
    """Replace ending in the url"""
    return os.path.dirname(url) + "/" + new_url_ending


def unpickle_file(path):
    """unpickle file"""
    with open("banner.p", "rb") as f:

        return pickle.load(f)


def draw_symbol_picture(picture_schema):
    """Draw picture from symbols basing on the input schema"""
    for line_schema in picture_schema:
        one_line_pict = []
        for symbol, count in line_schema:
            one_line_pict.append(symbol * count)
        print("".join(one_line_pict))


def main():
    """Run main function."""
    challenge_url = CHALL_URL
    page_text = common.get_page_content(challenge_url)
    if page_text:
        keyword = get_hidden_keyword(page_text)
    else:
        print("The page is empty")
        sys.exit()

    next_url = get_next_url(challenge_url, keyword)
    file_path = common.download_file(next_url)
    unpickled_object = unpickle_file(file_path)
    draw_symbol_picture(unpickled_object)

    next_challenge = common.get_next_challenge("channel")
    print(next_challenge)

    return next_challenge

if __name__ == "__main__":
    main()