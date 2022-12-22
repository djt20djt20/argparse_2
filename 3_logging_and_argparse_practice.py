import argparse
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)-15s %(message)s')
logger=logging.getLogger()

def go(arg):
    logger.info('this is the info that you passed in: {}'.format(args.message))

#this this file is executed as a script, then do this
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--message',type=str,help='type a message to be logged',required=False, default='default message')
    args = parser.parse_args()


    go(args)



 


