#!/usr/bin/python
import argparse
import yaml
from bottle import route, run, static_file
import logging

parser = argparse.ArgumentParser(description='Hello World')
parser.add_argument("--config", required=True)
parser.add_argument("--logging", required=True)
args = parser.parse_args()

class hello:
   def __init__(self, config, logconfig):
      self.config=config
      self.logger = logging.getLogger(logconfig["name"])
      handler = logging.FileHandler(logconfig["filename"])
      formatter = logging.Formatter(logconfig["format"])
      handler.setFormatter(formatter)
      self.logger.addHandler(handler) 
      self.logger.setLevel(logging.INFO)
   def sayhello(self):
      self.logger.info('Asked for a message')
      return config["message"]
   def start(self):
      run(host=self.config["host"], port=self.config["port"], debug=True)

logconfig = yaml.load(open(args.logging, 'r'))
config = yaml.load( open( args.config, 'r'))
helloapp=hello(config, logconfig)

@route('/favicon.ico')
def favicon():
   return static_file('static/favicon.ico', root='.')

@route('/')
def hello():
   return helloapp.sayhello()

helloapp.start()
