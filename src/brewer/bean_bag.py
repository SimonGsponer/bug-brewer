from abc import ABC, abstractmethod
from random import random, choice


from utils.dynamic_logger import Logger

class BasicBean:

    def __init__(self, n_calls: int, error_proc: float, logger:Logger) -> None:
        """f
        Args:
            n_calls: Number of function calls to perform.
            error_proc: Programmed random occurrence of error,
                must be between 0 and 1.
        """
        self.n_calls = n_calls
        self.error_proc = error_proc
        self.logger = logger
        self.error_occurred = False

    def __call__(self):
        self.logger.log.info(f"Starting execution of {self.n_calls} number of nodes")

        for i in range(self.n_calls):
            
            picked_callable = self.pick_callable()
            self.logger.log.info(f"Picked type{(str(picked_callable))}")
            picked_callable()
            if self.error_occurred:
                self.logger.log.info(f"Stopping execution…")
                break
    
    def node_1(self):
        self.logger.log.info("Invoking node 1...")
        self.logger.log.info("Node 1 completed as expected. Nothing weird going on here.")

    def node_2(self):
        self.logger.log.info("Invoking node 1...")
        self.logger.log.info("Node 2 finished without any issues. Everything looks good.")

    def node_3(self):
        self.logger.log.info("Invoking node 1...")
        self.logger.log.info("Node 3 ran as planned. No anomalies detected.")

    def node_4(self):
        self.logger.log.info("Invoking node 1...")
        self.logger.log.info("Node 4 completed perfectly. No irregularities to report.")

    def node_5(self):
        self.logger.log.info("Invoking node 1...")
        self.logger.log.info("Node 5 checked out fine. It's all clear on this end.")

    def node_6(self):
        self.logger.log.info("Invoking node 1...")
        self.logger.log.info("Node 6 concluded as expected. All clear, no surprises.")

    def node_7(self):
        self.logger.log.info("Invoking node 1...")
        self.logger.log.info("Node 7 has been successfully completed. Status: normal.")

    def node_8(self):
        self.logger.log.info("Invoking node 1...")
        self.logger.log.info("Execution of node 8 went off without a hitch. Nothing out of the ordinary.")

    def node_9(self):
        self.logger.log.info("Invoking node 1...")
        self.logger.log.info("Procedure of node 9 carried out successfully. Everything is in order.")

    @abstractmethod
    def error_node(self):
        """This is the node which will cause the crash!"""
        ...

    def pick_callable(self):
        """If procs, return node causing error. Otherwise, randomly choose healty node.
        """

        if random() > (1 - self.error_proc):
            return self.error_node

        else:
            nodes = [callable for callable in dir(self) if "node" in callable and "error_node" not in callable]
            node = choice(nodes)
            return getattr(self, node)


