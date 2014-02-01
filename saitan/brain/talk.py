from tweepy import API

class Talk():
	def __init__(self, oauth):
		self.api = API(auth_handler=oauth)

	def post(self, content, in_reply_to_status_id):
		self.api.update_status(content, in_reply_to_status_id)
