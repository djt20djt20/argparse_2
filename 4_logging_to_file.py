import logging
import argparse

logging.basicConfig(
    #path to file
    filename='my_log.log',
    
    #how verbose
    level=logging.INFO,
    
    #for writing the file
    filemode='w',

    #how the message appears
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

logger=logging.getLogger()

def go(args):
    logger.info('this is some info: {}'.format(args.info))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--info', type=str, help='add some info', required=False, default='default message')

    args = parser.parse_args()
    
    #run
    #sdohfiaosgh
    go(args)

