# twitterSearchParse.py
#
# Purpose: Returns a specificed number of results based on search string.
#          Parses JSON string into individual fields
#
# Athor:			RJ Podeschi
# Last Modified: 	11-09-2016
# 
# Notes: Requires Twitter API. From Python install directory, execute:
# python -m pip install twitter

import twitter
import json

ckey = 'CONSUMER_KEY_GOES_HERE'
csecret = 'CONSUMER_SECRET_GOES_HERE'
atoken = 'ACCESS_TOKEN_GOES_HERE'
asecret = 'ACCESS_SECRET_GOES_HERE'

auth = twitter.oauth.OAuth(atoken, asecret, ckey, csecret)
twitter_api = twitter.Twitter(auth=auth)

q = "#BlackHawks"
count = 50

search_results = twitter_api.search.tweets(q=q, count=count)

statuses = search_results['statuses']

status_texts = [ status['text']
                 for status in statuses ]

screen_names = [ user_mention['screen_name']
                 for status in statuses
                         for user_mention in status['entities']['user_mentions'] ]

hashtags = [ hashtag['text']
             for status in statuses
                     for hashtag in status['entities']['hashtags'] ]

#Compute a collection of all words from all tweets

words = [w
                 for t in status_texts
                         for w in t.split() ]

# Explore the first 5 items for each...

print(json.dumps(status_texts[0:5], indent=1))
print(json.dumps(screen_names[0:5], indent=1))
print(json.dumps(hashtags[0:5], indent=1))
print(json.dumps(words[0:5], indent=1))

for _ in range(5):
	print("Length of statuses", len(statuses))
	try:
		next_results = search_results['search_metadata']['next results']
	except KeyError as e:
		break
	
	kwargs = dict([ kv.split('=') for kv in next_results[1:].split("$") ])
	
	search_results = twitter_api.search.tweets(**kwargs)
	statuses += search_results['statuses']

print(json.dumps(statuses[0], indent=1))
