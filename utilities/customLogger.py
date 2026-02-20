"""import logging
import os
# https://tutorialsninja.com/demo/
class LogGen():
    @staticmethod
    def loggen():
        path = os.path.abspath(os.curdir) + '\\logs\\automation.log'
        logging.basicConfig(filename=path,
                            format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)
        return logger """

import logging
import os

class LogGen:
    @staticmethod
    def loggen():

        log_dir = "logs"
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        log_file = os.path.join(log_dir, "automation.log")

        logger = logging.getLogger("Test Login")
        logger.setLevel(logging.DEBUG)

        if not logger.handlers:   # prevents duplicate logs
            fileHandler = logging.FileHandler(log_file)
            formatter = logging.Formatter(
                "%(asctime)s : %(levelname)s : %(name)s : %(message)s"
            )
            fileHandler.setFormatter(formatter)
            logger.addHandler(fileHandler)

        return logger


