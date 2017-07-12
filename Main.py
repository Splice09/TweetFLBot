"""
The main script to execute twitter scraping for wordcloud data.
"""
# Import the necessary package to process data in JSON format
try:
    import json
except ImportError:
    import simplejson as json


# Import the necessary methods from "twitter" library
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream

#import credentials from credential file
from Credentials import *

#import player class
from Player import Player

def get_recent_tweet_ids_from_file():
    """
    Open and read from TweetID collection file to build a list used to
    set ID limits for timeline scraping.
    """
    my_file = open("TweetID.txt", "r")

    if my_file.mode == 'r':
        file_lines = my_file.readlines()
        player_list = [Player(line.split(",")[0], line.split(",")[1]) for line in file_lines]

    my_file.close()
    return player_list

O_AUTH = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

# Initiate the connection to Twitter REST API
TWITTER = Twitter(auth=O_AUTH)

#Call function to obtain recent TweetIds from file
PLAYER_LIST = get_recent_tweet_ids_from_file()

# Print each tweet in the stream to the screen
for player in PLAYER_LIST:
    #Fetch twitter data
    ITERATOR = TWITTER.statuses.user_timeline(screen_name=player.tsn,since_id = player.tid,exclude_replies="true")
    
    # Print list of tweets
    for tweet in ITERATOR:
        
        # Twitter Python Tool wraps the data returned by Twitter
        # as a TwitterDictResponse object.
        # We convert it back to the JSON format to print/score
        print json.dumps(tweet['id'])
        print json.dumps(tweet['user']['name'])
        print json.dumps(tweet['user']['screen_name'])
        print json.dumps(tweet['created_at'])
        print json.dumps(tweet['text'])
        print ''   


print ''
print "Tweet fetch complete."
print ''

