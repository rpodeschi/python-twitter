# twitterSearch.py
#
# Purpose: Returns a specificed number of results based on search string.
#          
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
