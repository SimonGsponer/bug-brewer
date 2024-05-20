"""

TODO:
* based on error case, create error report using LLM
* langchain + OpenAI API

"""
from brewer.barista import coffee_factory
from utils.dynamic_logger import Logger

logger = Logger()

logger.log.info("Hi")

def main():

    for i in range(10):

        logger.reroute_logs(tar_file=f"error_case_{i}.log")
        logger.log.info("Starting execution...")

        buggy_coffee = coffee_factory(logger=logger)        
        buggy_coffee.logger.log.info(f"I am {type(buggy_coffee)}")
        buggy_coffee()
        print(buggy_coffee.error_types)
        # this works


if __name__=="__main__":
    main()