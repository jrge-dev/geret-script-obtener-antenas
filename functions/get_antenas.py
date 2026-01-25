from model.antenas import Antenas
from loguru import logger

def get_antenas():
    antena = Antenas()
    antenas_activas = antena.get_antenas_activas()
    logger.info(f"Se encontraron {antenas_activas.__len__()} activas")
    for row in antenas_activas:
        print(row)
