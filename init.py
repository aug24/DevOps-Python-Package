import argparse
import yaml
import hello

parser = argparse.ArgumentParser(description='Hello World')
parser.add_argument("config", required=True)
parser.add_argument("logging", required=True)
args = parser.parse_args()

logging = yaml.load(open(args.logging, 'r'))
config = yaml.load( open( args.config, 'r'))

hello=hello(config, logging)
