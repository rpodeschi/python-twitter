# twitterSearch.py
#
# Purpose: Use a listener to wait on new tweets with a given search parameter
#
# Athor:		RJ Podeschi
# Last Modified: 	11-09-2016
# 
# Notes: Requires Tweepy. From Python install directory, execute:
# python -m pip install tweepy

import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

ckey = 'CONSUMER_KEY_GOES_HERE'
csecret = 'CONSUMER_SECRET_GOES_HERE'
atoken = 'ACCESS_TOKEN_GOES_HERE'
asecret = 'ACCESS_SECRET_GOES_HERE'

class MyListener(StreamListener):

	def on_data(self, data):
		print(data)
		return True
	
	def on_error(self, status):
		print(status)
	
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
api = tweepy.API(auth)
twitterStream = Stream(auth, MyListener())
# Change value in next line for search string
twitterStream.filter(track=["Trump"])
# When you want the stream to stop in Python Shell, use ctrl+c
	
	
