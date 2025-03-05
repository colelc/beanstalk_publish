import sys
import greenstalk
from src.config.config import Config
from src.logging.app_logger import AppLogger


class BeanstalkService(object):
    beanstalk_client = None
    #ENV = "d" # default to development environment
   
    @staticmethod
    def set_up_client() -> type:
        logger = AppLogger.get_logger()

        beanstalk_server = Config.get_property("beanstalk.server")
        beanstalk_port = Config.get_property("beanstalk.port")
        
        try:
            # Connect to the Beanstalk server
            beanstalk_client = greenstalk.Client((beanstalk_server, beanstalk_port))
            logger.info("we have a beanstalk client")
            logger.info(str(type(beanstalk_client)) + " " + str(beanstalk_client))
        except Exception as e:
            logger.error(str(e))
            sys.exit(99)

        return beanstalk_client

    @staticmethod
    def get_beanstalk_client():
        if BeanstalkService.beanstalk_client is None:
            BeanstalkService.beanstalk_client = BeanstalkService.set_up_client()
            
        return BeanstalkService.beanstalk_client
    
    @staticmethod
    def beanstalk_watcher():
        log = AppLogger.get_logger()

        log.info("Waiting for jobs...")
        while True:
            try:
                # Reserve a job from the queue
                job = BeanstalkService.get_beanstalk_client().reserve()
                log.info("A job is reserved from the queue")
                
                # Process the job
                BeanstalkService.process_job(job)
                
                # Delete the job after processing
                BeanstalkService.get_beanstalk_client().delete(job)
            except greenstalk.TimedOutError:
                log.info("No jobs available, waiting...")
            except Exception as e:
                log.error(f"Error processing job: {e}")
                # You might want to bury or release the job here
                BeanstalkService.get_beanstalk_client().bury(job)
    
    @staticmethod
    def process_job(job):
        log = AppLogger.get_logger()
        # Replace this with your actual job processing logic
        print(f"Processing job: {job.body}")
        log.info("Processing job: " + str(job))
        log.info(str(job.body))
        # Execute your command here
    
