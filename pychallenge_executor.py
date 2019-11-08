import os
import re
import logging
from importlib import import_module

CHALL_REGEX = "pychallenge_\d.py$"
CHALL_PTRN = "pychallenge_{}.py"


class ChallengeExecutor:

    def __init__(self, path):
        self.path = path


    def get_all(self):
        """Return a sorted list of pychallenge_x.py file names found in the
        ChallengeExecutor.path directory
        """
        challenge_files = []
        for file in os.scandir(self.path):
            if file.is_file():
                if re.match(CHALL_REGEX, file.name):
                    challenge_files.append(file.name)

        return sorted(challenge_files)

    def run(self, number):
        """Execute pychallenge specified by its number"""
        if type(number) is not int:
            raise TypeError("Integer value is expected")
        if not 1 <= number <= 33:
            raise ValueError("Only values in range 1..33 are allowed")

        chall_name = CHALL_PTRN.format(number)
        if chall_name in self.get_all():
            challenge = import_module(chall_name[:-3])
            next_ch_link = challenge.execute()
            return next_ch_link
        else:
            raise ModuleNotFoundError(chall_name)


    def run_all(self):
        pass


    def generate_emty(self):
        pass


def configure_logger():

    logger = logging.getLogger('pychallenge_executor')
    logger.setLevel(logging.DEBUG)
    # fh = logging.FileHandler('spam.log')
    # fh.setLevel(logging.DEBUG)
    # create console handler with a higher log level
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    # create formatter and add it to the handlers
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    # fh.setFormatter(formatter)
    ch.setFormatter(formatter)
    # add the handlers to the logger
    # logger.addHandler(fh)
    logger.addHandler(ch)

    return logger


if __name__=="__main__":
    logger = configure_logger()
    logger.info("Start of application")
    executor = ChallengeExecutor('./')
    challenges = executor.get_all()
    print(challenges)
    next_link = executor.run(2)
    print(next_link)