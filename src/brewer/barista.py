from random import choice

import numpy as np

from .chaos_coffees import (
    EspressoError,
    DoppioDisruptor,
    MacchiatoMalfunction,
    FrappeFrenzy,
    CorruptedCortado,
    AnomalousAmericano,
    RogueRistretto,
    MochaMayhem,
    LeakyLatte,
    PerturbedPocillo
)
from utils.dynamic_logger import Logger


def coffee_factory(logger: Logger):

    n_calls = choice([n for n in range(100, 1000, 100)])

    proc_rate = choice(np.arange(0.01,0.1,0.01).tolist())

    picked_class = choice(
        [
            EspressoError,
            DoppioDisruptor,
            MacchiatoMalfunction,
            FrappeFrenzy,
            CorruptedCortado,
            AnomalousAmericano,
            RogueRistretto,
            MochaMayhem,
            LeakyLatte,
            PerturbedPocillo
         ]
    )
    
    logger.log.info(f"n_calls: {n_calls}, proc_rate: {proc_rate}")

    return picked_class(n_calls=n_calls, error_proc=proc_rate, logger=logger)

    