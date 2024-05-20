import sys
import logging
import traceback
from pathlib import Path

class Logger:

    def __init__(self, tar_file: str="default.log", tar_dir="data"):

        self.tar_file = tar_file
        self.tar_dir = tar_dir
        self.current_handler = None

        self.log = logging.getLogger(__name__)
        logging.basicConfig(filename='bugbrewer.log', encoding='utf-8', level=logging.DEBUG)
        self.set_file_handler()

        self.log.info("Logger instantiated")

    
    def set_file_handler(self):
        
        if self.current_handler:
            self.log.info(f"Removing handler: {self.current_handler}")
        self.log.removeHandler(self.current_handler)

        log_fp = Path().resolve().joinpath(self.tar_dir).joinpath(self.tar_file)

        self.current_handler = logging.FileHandler(log_fp.as_posix())
        self.current_handler.setLevel(logging.DEBUG)

        formatter = logging.Formatter('%(asctime)s - %(filename)s - %(lineno)s - %(levelname)s - %(message)s')
        self.current_handler.setFormatter(formatter)

        self.log.addHandler(self.current_handler)
        self.log.info(f"Added new handler: {log_fp}")

    
    def reroute_logs(self, tar_file, tar_dir=None):
        
        self.tar_file = tar_file
        if tar_dir:
            self.tar_dir = tar_dir
        
        self.set_file_handler()
        self.log.info("Logs have been rerouted.")

    def log_error(self, exception_to_log):
        text = "".join(traceback.format_exception(exception_to_log))
        self.log.error("An exception occurred: %s", text)

