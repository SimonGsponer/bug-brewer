"""

TODO:
* based on error case, create error report using LLM
* langchain + OpenAI API

"""
import time
from pathlib import Path
from dotenv import load_dotenv

from brewer.barista import coffee_factory
from documentarian.report import ReportGenerator
from utils.dynamic_logger import Logger
from utils.config import Settings

logger = Logger()

load_dotenv()

logger.log.info("Hi")
report_generator = ReportGenerator(settings=Settings())

def main():

    for i in range(100):

        name_logfile = f"error_case_{i}.log"
        name_report = f"report_{i}.txt"

        logger.reroute_logs(tar_file=name_logfile)
        logger.log.info("Starting execution...")

        buggy_coffee = coffee_factory(logger=logger)        
        buggy_coffee.logger.log.info(f"I am {type(buggy_coffee)}")
        buggy_coffee()
        print(buggy_coffee.error_types)
        time.sleep(10)
        with open(logger.log_fp, 'r') as f:
            error_logfile = f.read()

        report_generator(
            errors=str([err.error for err in buggy_coffee.error_types]),
            resolutions=str([err.resolution for err in buggy_coffee.error_types]),
            error_log=error_logfile,
            name_report=name_report
        )
        # this works


if __name__=="__main__":
    main()
    