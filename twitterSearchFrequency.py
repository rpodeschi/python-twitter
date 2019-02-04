# twitterSearchFrequency.py
#
# Purpose: Returns summary data on frequency of tweets with search string
#          
#
# Athor:			RJ Podeschi
# Last Modified: 	11-09-2016
# 
# Notes: Requires Twitter API, Counter, PrettyTable. From Python install directory, execute:
#        python -m pip install twitter
#		 python -m pip install prettytable
#		 python -m pip install counter

import twitter
import json
from prettytable import PrettyTable
from collections import Counter

ckey = 'CONSUMER_KEY_GOES_HERE'
csecret = 'CONSUMER_SECRET_GOES_HERE'
atoken = 'ACCESS_TOKEN_GOES_HERE'
asecret = 'ACCESS_SECRET_GOES_HERE'

auth = twitter.oauth.OAuth(atoken, asecret, ckey, csecret)
twitter_api = twitter.Twitter(auth=auth)

q = "Disney"
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

for label, data in (('Words', words),
                     ('Screen Name', screen_names),
                     ('Hashtag', hashtags)):
        pt = PrettyTable(field_names=[label, 'Count'])
        c = Counter(data)
        [ pt.add_row(kv) for kv in c.most_common()[:30] ]
        pt.align[label], pt.align['Count'] = '1', 'r' # Set Column alignment
        print(pt)
