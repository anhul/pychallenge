"""Python challenge number 3."""

import re
from utils import common

CHALL_LINK = "http://www.pythonchallenge.com/pc/def/equality.html"
HIDDEN_WORD_PATTERN = r"[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]"


def main():
    """Run main function."""
    challenge_page_link = CHALL_LINK
    raw_html = common.get_page_content(challenge_page_link)

    if raw_html:
        commented_text = common.get_text_in_comments(raw_html)
        found_letters = re.findall(HIDDEN_WORD_PATTERN, commented_text[0])

        if found_letters:
            hidden_word = "".join(found_letters)
            next_challenge = common.get_next_challenge(hidden_word)
            print(next_challenge)
            return next_challenge

    return None


if __name__ == "__main__":
    main()
