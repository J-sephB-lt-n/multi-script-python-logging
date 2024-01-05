import logging

import module1
import module2

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

if __name__=="__main__":
    logger.info("this is a log message from main.py")
    module1.explain()
    module2.explain()
