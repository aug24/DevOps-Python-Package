#!/usr/bin/python
from bottle import route, run, template

def hello(config, logging):
  @route('/')
  def HelloWorld(env):
    logging.log('Asked for a message')
    return template(config.message)

