from src.config.config import Config
from src.logging.app_logger import AppLogger
from src.services.beanstalk_service import BeanstalkService
import greenstalk

## https://www.perplexity.ai/search/how-can-i-write-a-python-progr-T.BI3UbIQ_mW2V5XRp34xQ
## https://greenstalk.readthedocs.io/en/stable/api.html
class App(object):

    @classmethod
    def go(cls):
        log = AppLogger.get_logger()
        log.info("")
        log.info("This is code to place a message on a beanstalk queue")
        log.info("")

        config = Config.get_config()

        beanstalk_client = BeanstalkService.get_beanstalk_client()
        tubes = beanstalk_client.watch(Config.get_property("tube"))

        BeanstalkService.beanstalk_watcher()



        log.info("DONE")

App.go()