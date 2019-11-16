import os
import re
from configs import configure_logger, CH_SRC_TEMP, CH_TEST_TEMP
from importlib import import_module

CH_REGEX = "challenge_\d.py$"
CH_PTRN = "challenge_{}.py"
CH_FIRST = 0
CH_LAST = 33


class ChallengeExecutor:

    def __init__(self, path):
        self.path = path
        self.logger = configure_logger("executor")
        self.ch_number_to_url = {}
        self.ch_number_to_url[0] = "http://www.pythonchallenge.com/pc/def/0.html"


    def get_all(self):
        """Return a sorted list of pychallenge_x.py file names found in the
        ChallengeExecutor.path directory
        """
        self.logger.info("Find all challenge files in {}".format(
            os.path.abspath(self.path)))
        challenge_files = []
        for file in os.scandir(self.path):
            if file.is_file():
                if re.match(CH_REGEX, file.name):
                    challenge_files.append(file.name)
        self.logger.debug("{} challenge files found: {}".format(
            len(challenge_files),
            sorted(challenge_files)))

        return sorted(challenge_files)

    def run(self, number):
        """Execute challenge specified by its number"""
        if type(number) is not int:
            raise TypeError("Integer value is expected")
        if not CH_FIRST <= number <= CH_LAST:
            raise ValueError("Only values in range {}..{} are allowed"
                             .format(CH_FIRST, CH_LAST))

        ch_name = CH_PTRN.format(number)
        if ch_name in self.get_all():
            ch_module = import_module(ch_name[:-3])
            self.logger.info("{} execution started".format(ch_name))
            next_ch_url = ch_module.execute()
            if next_ch_url:
                self.logger.info("{} execution successfully finished".format(
                    ch_name))
            else:
                self.logger.warning("{} execution failed".format(ch_name))
            return next_ch_url
        else:
            raise ModuleNotFoundError(ch_name)


    def run_all(self):
        pass


    def generate_files(self, number, ch_url="", src_file=True, test_file=False):
        """ Generate challenge source and test files from template"""
        if src_file:
            ch_file_path = os.path.join(self.path, CH_PTRN.format(number))
            if os.path.isfile(ch_file_path):
                self.logger.info("File {} already exists".format(ch_file_path))
            else:
                # Read source code file template
                with open(CH_SRC_TEMP, "r") as fp:
                    ch_src_template = fp.read()
                ch_src = ch_src_template.format(number=number,
                                                ch_number=number,
                                                ch_url=ch_url)
                # Create source file using template
                with open(ch_file_path, "w") as fp:
                    fp.write(ch_src)
                self.logger.info("File {} successfully created".format(ch_file_path))

        if test_file:
            pass


if __name__=="__main__":

    executor = ChallengeExecutor('./')
    # next_link = executor.run(7)
    executor.generate_files(1,"http://www.pythonchallenge.com/pc/def/274877906944.html")
