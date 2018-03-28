#!/usr/local/bin/python3

import logging
import argparse
import sys
#######################################
appName = "cli_template"
#######################################
# get an argparser object
argParser = argparse.ArgumentParser(
    description='''Description of cli_template goes here''',
    epilog='''Example:
    cli_template (args)
    ''',
    formatter_class=argparse.RawDescriptionHelpFormatter
)

# allow user to set log level on command line
argParser.add_argument('--loglevel', help='Set log level on console (optional, default=info). Use one of: "critical" "error" "warning" "info" "debug"', default="info")

# parse args
args = argParser.parse_args()

#######################################
# sanity checks
logLevel = args.loglevel.lower()
if (logLevel not in ['critical', 'error', 'warning', 'info', 'debug']):
    print('Invalid log level "' + logLevel + "'")
    sys.exit(1)
#######################################
# Set up logging

if (logLevel == 'critical'):
    consoleLogLevel = logging.CRITICAL
elif (logLevel == 'error'):
    consoleLogLevel = logging.ERROR
elif (logLevel == 'warning'):
    consoleLogLevel = logging.WARNING
elif (logLevel == 'debug'):
    consoleLogLevel = logging.DEBUG
else:
    # use INFO by default
    consoleLogLevel = logging.INFO

logging.getLogger().setLevel(logging.DEBUG)
logger = logging.getLogger(appName)

# create file handler which logs even debug messages
fh = logging.FileHandler('/var/log/' + appName + '.log')
fh.setLevel(logging.INFO)

# create console handler
ch = logging.StreamHandler()
ch.setLevel(consoleLogLevel)

# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)
# add the handlers to the logger
logger.addHandler(fh)
logger.addHandler(ch)
#######################################

logger.debug('this is a debug message')
logger.info('this is an info message')
logger.warning('this is a warning message')
logger.error('this is an error message')
logger.critical('this is a critical message')
