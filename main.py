from loguru import logger
from functions.get_antenas import get_antenas
from time import sleep


if __name__ == "__main__":
    logger.add("logs.log", level="DEBUG")
    logger.success("Inicio del proceso")
    while True:
        get_antenas()
        sleep(10)


