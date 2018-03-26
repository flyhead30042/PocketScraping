import logging
import configparser
from datetime import datetime
import os


# Generic configuration
DATESTAMP1 = datetime.now().strftime("%Y%m%d")
TIMESTAMP1 = datetime.now().strftime("%Y%m%d_%H%M%S")
TIMESTAMP2 = datetime.now().strftime("%Y%m%d_%a_%I%M%S_%p")

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

LOG_DIR = os.path.join(ROOT_DIR+"\..", "log")

LOGGING_LEVEL = logging.DEBUG
logfilename = os.path.join(LOG_DIR, DATESTAMP1+ ".log")
logging.basicConfig(level=LOGGING_LEVEL,
                    format=' %(asctime)s - %(levelname)s - %(message)s',
                    handlers=[logging.FileHandler(logfilename, 'w', 'utf-8')])

console = logging.StreamHandler()
logging.getLogger('').addHandler(console)

# Project configuration
CONSUMER_KEY="74406-8a08d271e96900d77476c4dc"

config = configparser.ConfigParser()
config.read(os.path.join(ROOT_DIR, 'pocketman.ini'))
