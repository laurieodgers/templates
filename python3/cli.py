#!/usr/local/bin/python3

import logging
import argparse
import sys
import os
#######################################
appName = "cli_template"
version = "1.0.0"
#######################################
# get the filename and directory of this app
appFilename = os.path.basename(__file__)
appDirectory = os.path.dirname(os.path.realpath(__file__))

# get an argparser object
argParser = argparse.ArgumentParser(
    description='''Description of cli_template goes here''',
    epilog="Example:\n  " + appFilename + " -l warning",
    formatter_class=argparse.RawDescriptionHelpFormatter
)

argParser.add_argument('-d', '--debug', help='Enable debug mode. Equivalent to `-l debug`', action='store_true')
argParser.add_argument('-l', '--loglevel', help='Set log level on console', default="info", choices=['critical', 'error', 'warning', 'info', 'debug'], type=str.lower)
argParser.add_argument('-q', '--quiet', help='Prevents any log output to the console. Logs will still be sent to the output file.', action='store_true')
argParser.add_argument('-v', '--version', help='Prints the version of this command', action='store_true')

# parse args
args = argParser.parse_args()

#######################################
# print version
if (args.version):
    print(appFilename + ' (' + appName + ')' + ' ' + version)
    sys.exit(0)

if (args.debug):
    args.loglevel = 'debug'

#######################################
# Set up logging

if (args.loglevel == 'debug'):
    consoleLogLevel = logging.DEBUG
elif (args.loglevel == 'warning'):
    consoleLogLevel = logging.WARNING
elif (args.loglevel == 'error'):
    consoleLogLevel = logging.ERROR
elif (args.loglevel == 'critical'):
    consoleLogLevel = logging.CRITICAL
else:
    # use INFO by default
    consoleLogLevel = logging.INFO

logging.getLogger().setLevel(logging.DEBUG)
logger = logging.getLogger(appName)

# create file handler which logs even debug messages
fh = logging.FileHandler('/var/log/' + appName + '.log')
fh.setLevel(logging.INFO)

# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

fh.setFormatter(formatter)
logger.addHandler(fh)

# create console handler if quiet wasnt requested
if (not args.quiet):
    ch = logging.StreamHandler()
    ch.setLevel(consoleLogLevel)
    ch.setFormatter(formatter)
    logger.addHandler(ch)

#######################################

logger.debug('this is a debug message')
logger.info('this is an info message')
logger.warning('this is a warning message')
logger.error('this is an error message')
logger.critical('this is a critical message')
