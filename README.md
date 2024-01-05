# multi-script-python-logging

This repo illustrates how imported modules (.py scripts) inherit their logging format from the script which imported them (main.py).

```python
# module1.py # 
import logging
logger = logging.getLogger(__name__)
def explain():
    logger.info("this is a log message from module1.py")

# module2.py #
import logging                                                                                                                                           
logger = logging.getLogger(__name__)
def explain():
    logger.info("this is a log message from module2.py")

# main.py #
import logging
import module1
import module2

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

if __name__=="__main__":
    logger.info("this is a log message from main.py")
    module1.explain()
    module2.explain()
```

```bash
~$ python main.py
2024-01-05 16:32:09,132 - __main__ - INFO - this is a log message from main.py
2024-01-05 16:32:09,132 - module1 - INFO - this is a log message from module1.py
2024-01-05 16:32:09,132 - module2 - INFO - this is a log message from module2.py
```
