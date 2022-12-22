import argparse
import logging
# logging is used so that you don't have to use print statements

# configure, format tells how to display the message, level defines how verbose it is.
logging.basicConfig(level=logging.INFO, format='%(asctime)-15s %(message)s')

#create logger object to print
logger = logging.getLogger()

logger.info('This is a message')
logger.warning('This is a warning')
logger.error('This is an error')