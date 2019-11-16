"""Python challenge number 4."""
#!/usr/local/bin/python3
import os
import re
from bs4 import BeautifulSoup
from utils import common

CHALL_LINK = "http://www.pythonchallenge.com/pc/def/linkedlist.html"

def get_first_nothing(page_text):
    """Get the first nothing from the initial html page"""
    soup = BeautifulSoup(page_text, features="html.parser")
    center = soup.find("center")
    match_obj = re.search(r"=(\d+)", center.a["href"])
    if match_obj:
        return match_obj.group(1)

    return None

def get_next_nothing(page_text):
    """Get the next nothing"""
    nothing_ptrn = re.compile(r"next nothing is (\d+)")
    match_obj = nothing_ptrn.search(page_text)
    if match_obj:
        return match_obj.group(1)

    return None

def main():
    """Run main function."""
    challenge_page_link = CHALL_LINK
    f_name, _ = os.path.splitext(challenge_page_link)
    challenge_page_link = f_name + ".php"

    raw_html = common.get_page_content(challenge_page_link)
    if raw_html:
        nothing = get_first_nothing(raw_html)
        if nothing:
            print(nothing)
            url_params = {"nothing": nothing}
            next_nothing = nothing

            for i in range(400):

                next_response = common.get_page_content(challenge_page_link, url_params)
                prev_nothing = next_nothing
                next_nothing = get_next_nothing(next_response)

                print(f"{i}    {next_nothing}")

                if next_nothing is None:
                    if i == 85:
                        next_nothing = str(int(int(prev_nothing)/2))
                    else:
                        break
                url_params["nothing"] = next_nothing





            # next_challenge = pychallenge_common.get_next_challenge(hidden_word)
            # print(next_challenge)
            # return next_challenge

    return None


if __name__ == "__main__":
    main()