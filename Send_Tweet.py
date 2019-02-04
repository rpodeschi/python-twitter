# Sent_Tweet.py
#
# Purpose: Uses Tweepy package to send Twitter status update
#
# Athor:	        RJ Podeschi
# Last Modified: 	11-09-2016
# 
# Notes: Requires Tweepy API. From Python install directory, execute:
# python -m pip install tweppy==3.5.0

import tweepy
from tweepy import OAuthHandler
 
consumer_key = 'CONSUMER_KEY_GOES_HERE'
consumer_secret = 'CONSUMER_SECRET_GOES_HERE'
access_token = 'ACCESS_TOKEN_GOES_HERE'
access_secret = 'ACCESS_SECRET_GOES_HERE'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)

api.update_status(status="#IS470 - I just uploaded Send_Tweet.py to Moodle to send Tweets using Python and Tweepy. I used the script to send this tweet.")
