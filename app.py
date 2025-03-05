from src.config.config import Config
from src.logging.app_logger import AppLogger

class App(object):

    def __init__(self) -> None:
        log = AppLogger.get_logger()
        log.info("")
        log.info("__init__ This is code to place a message on a beanstalk queue")
        log.info("")

        config = Config.get_config()
    


    @classmethod
    def go(cls):
        log = AppLogger.get_logger()
        log.info("")
        log.info("This is code to place a message on a beanstalk queue")
        log.info("")

        log.info("DONE")

App.go()