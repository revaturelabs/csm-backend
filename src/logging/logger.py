
'''Logging module'''
import logging
import logging.config
from os import path

log_file_path = path.join(path.dirname(path.abspath(__file__)), 'log.conf')
print(path.dirname(path.abspath(__file__)))
logging.config.fileConfig(log_file_path)
#logging.info('this is the root logger')
def get_logger(nom):
    '''returns a logger for the module that called the function'''
    return logging.getLogger(nom)
