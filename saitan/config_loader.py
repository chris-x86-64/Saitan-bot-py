import sys
import yaml
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-c", "--config", action = "store", dest = "config_file", help = "config file in yaml format.")
(options, args) = parser.parse_args()

try:
	stream = open(options.config_file, 'r')
except TypeError, e:
	print e
	print "Please specify the path to config file (--config CONFIG_FILE)"
	sys.exit(1)
except IOError, e:
	print e
	print "Specified config file not found!"
	sys.exit(1)

config = yaml.load(stream)
print config
