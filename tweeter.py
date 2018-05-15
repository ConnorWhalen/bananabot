import json
import tweepy

cred_file = open('credentials')
cred_str = cred_file.read()
cred_json = json.loads(cred_str)

auth = tweepy.OAuthHandler(cred_json['consumer_key'], cred_json['consumer_secret'])
auth.set_access_token(cred_json['access_token'], cred_json['access_token_secret'])

api = tweepy.API(auth)

def post_tweet(text):
	api.update_status(text)
