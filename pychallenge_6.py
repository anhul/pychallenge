"""Python challenge number 6."""

import re
import zipfile
import pychallenge_common

CHALL_URL = "http://www.pythonchallenge.com/pc/def/channel.html"

def extract_zip(file_path, destination):
    with zipfile.ZipFile(file_path, 'r') as zip_ref:
        zip_ref.extractall(destination)
        scan_files(destination, zip_ref)


def scan_files(files_path, zip_ref):
    scan = True
    next_nothing = "90052"
    comment_bytes = bytearray()

    while scan:
        with open(f"{files_path}/{next_nothing}.txt") as f:
            comment_byte = zip_ref.getinfo(f"{next_nothing}.txt").comment
            comment_bytes += comment_byte
            text = f.read()
            next_nothing = get_next_nothing(text)
            if next_nothing is None:
                scan = False
                # print(text)

    print(comment_bytes.decode("ascii"))
    #TODO find out the difference between UTF-8 and ASCII

def get_next_nothing(text):
    """Get the next nothing"""
    nothing_ptrn = re.compile(r"^Next nothing is (\d+)$")
    match_obj = nothing_ptrn.search(text)
    if match_obj:
        return match_obj.group(1)

    return None


def main():
    """Run main function."""
    next_url = pychallenge_common.replace_file_ext(CHALL_URL, "zip")
    file_path = pychallenge_common.download_file(next_url)
    destination = "./data"
    extract_zip(file_path, destination)

    next_challenge = pychallenge_common.get_next_challenge("hockey")
    print(next_challenge)

    return next_challenge

if __name__ == "__main__":
    main()