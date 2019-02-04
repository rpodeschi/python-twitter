# Get10FeedItems

import tweepy
from tweepy import OAuthHandler
 
consumer_key = 'CONSUMER_KEY'
consumer_secret = 'CONSUMER_SECRET'
access_token = 'ACCESS_TOKEN'
access_secret = 'ACCESS_SECRET'
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)
   
for status in tweepy.Cursor(api.home_timeline).items(10):
    print(status.text)
    print("\n")
