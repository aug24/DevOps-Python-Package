#!/usr/bin/python
from bottle import route

def hello(config, logging):
  @route('/')
  def HelloWorld(env):
    logging.log('Asked for a message')
    return config.message

