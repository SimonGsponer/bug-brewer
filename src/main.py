"""

* Don't log with Syslog - log to folder in application directory and mount that directory

https://stackoverflow.com/questions/6386698/how-to-write-to-a-file-using-the-logging-python-module

"""
from utils.dynamic_logger import Logger

logger = Logger()

logger.log.info("Hi")

def main():

    logger.log.info("Logging into initial file")

    logger.reroute_logs(tar_file="error_case_1.log")
    logger.log.info("yeet")
    try:
        10 / 0
    except Exception as e:
        logger.log_error(exception_to_log=e)


if __name__=="__main__":
    print("Hello world!")
    main()