import tweepy
from saitan.brain import fav, talk

class StreamListener(tweepy.StreamListener):
	def __init__(self, config, oauth):
		super(StreamListener, self).__init__()
		self.api = tweepy.API(auth_handler = oauth)
		self.config = config
		self.me = self.api.me()
		self.talk_interface = talk.Talk(oauth)
		self.fav_interface = None

	def on_connect(self):
		print "[INFO] Starting saitan-bot."

	def on_status(self, status):
		if hasattr(status, "retweeted_status"):
			print "[DEBUG] Retweets are ignored."
			return

		try:
			print status.text
			return
		except:
			pass

		try:
			print status.event
			return
		except:
			pass

		raise

	def on_error(self, code):
		print code
		return False
