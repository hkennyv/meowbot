import configparser
import logging

log = logging.getLogger(__name__)

parser = configparser.ConfigParser()
parser.read("config.ini")

config = dict(parser["DEFAULT"])

log.info(f"config loaded: {config}")
