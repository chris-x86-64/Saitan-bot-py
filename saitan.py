from optparse import OptionParser
from saitan.config_loader import Config

parser = OptionParser()
parser.add_option("-c", "--config", action = "store", dest = "config_file", help = "config file in yaml format.")
(options, args) = parser.parse_args()

config = Config(options.config_file)
print config.OAuthKeys()
