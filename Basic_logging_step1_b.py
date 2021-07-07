import logging
import os

# Specify the location of the logfile.
logfilename=os.path.join(os.path.dirname(os.path.realpath(__file__)), 'my_application.log')

# Print to stdout and also send to file.
logging.basicConfig(
    level=logging.DEBUG,
    format='[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s',
    datefmt='%d-%m-%Y:%H:%M:%S',
    handlers=[
        logging.FileHandler(logfilename, mode='a'),
        logging.StreamHandler()
    ]
)

#Lets print some log message.
logging.debug('This will get logged to file and console')
