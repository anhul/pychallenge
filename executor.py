import os
import re
from configs import configure_logger, LOGGER_NAME
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


if __name__=="__main__":
    logger = configure_logger(LOGGER_NAME)
    logger.info("Challenge executor is created")
    logger.debug("Logger id is {}".format(id(logger)))
    executor = ChallengeExecutor('./')
    challenges = executor.get_all()
    next_link = executor.run(2)
    logger.info(next_link)