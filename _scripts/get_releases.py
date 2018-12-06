#!/usr/bin/env python

import configparser
import argparse

# Parsing arguments
parser = argparse.ArgumentParser()
parser.add_argument('-c', '--config', help='config file', required=True)
args = parser.parse_args()

config = configparser.ConfigParser()
config.read(args.config)

list=config['releases']['registered'].split(',')

for r in list:
   print r



