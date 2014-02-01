# -*- coding: utf-8 -*-

from optparse import OptionParser
from saitan.config_loader import Config
from saitan.oauth_handler import SaitanOAuthHandler
from saitan.listener import Stream
import sys

parser = OptionParser()
parser.add_option("-c", "--config", action = "store", dest = "config_file", help = "config file in yaml format.")
parser.add_option("-t", "--test-mode", action = "store_true", dest = "test_mode", default = False, help = "Post a test tweet then exit.")
(options, args) = parser.parse_args()

config = Config(options.config_file)
oauth = SaitanOAuthHandler(config).authenticate()

if options.test_mode == False:
	streamer = Stream(config, oauth)
	try:
		streamer.userstream()
	except KeyboardInterrupt:
		print "[CRITICAL] Exiting saitan-bot on SIGINT. Good bye."
		sys.exit(0)
else:
	print "[DEBUG] Testing mode initiated."
	try:
		from tweepy import API
		from saitan.brain.talk import Talk
		interface = Talk(API(auth_handler=oauth))
		interface.post(u"さいたんbot is initiating self test...", None)
		sys.exit(0)
	except:
		raise
