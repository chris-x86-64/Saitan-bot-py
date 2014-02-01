import tweepy

class StreamListener(tweepy.StreamListener):
	def __init__(self, config):
		super(StreamListener, self).__init__()
		self.config = config

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
