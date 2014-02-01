from optparse import OptionParser
from saitan.config_loader import Config
from saitan.listener import StreamListener
from tweepy import OAuthHandler, Stream
import sys

parser = OptionParser()
parser.add_option("-c", "--config", action = "store", dest = "config_file", help = "config file in yaml format.")
(options, args) = parser.parse_args()

config = Config(options.config_file)

keys = config.OAuthKeys()
oauth = OAuthHandler(keys['consumer_key'],
		keys['consumer_secret'],
		secure = True
		)
oauth.set_access_token(keys['access_token_key'], keys['access_token_secret'])

listener = StreamListener(config)
streamer = Stream(auth = oauth, listener = listener)
try:
	streamer.userstream()
except KeyboardInterrupt:
	print "[CRITICAL] Exiting saitan-bot on SIGINT. Good bye."
	sys.exit(0)
