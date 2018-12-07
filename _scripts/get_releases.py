#!/usr/bin/env python

import configparser
import argparse

# Parsing arguments
parser = argparse.ArgumentParser()
parser.add_argument('-c', '--config', help='config file', required=True)
parser.add_argument('-r', '--release', help='release section' )
parser.add_argument('-a', '--application', help='application section' )
args = parser.parse_args()

config = configparser.ConfigParser()
config.read(args.config)

if args.application:
  print config[args.application]['jobname']
  exit(0)


if args.release: 
  list=config[args.release]['application'].split(',')
  for app in list:
    print app
  exit(0)

# print releases
list=config['releases']['registered'].split(',')
for r in list:
   print r



