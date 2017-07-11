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

O_AUTH = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

# Initiate the connection to Twitter Streaming API
TWITTER_STREAM = TwitterStream(auth=O_AUTH)

#Call function to obtain recent TweetIds from file
PLAYER_LIST = get_recent_tweet_ids_from_file()

# Returns a collection of the most recent Tweets posted by the user
# indicated by the screen_name or user_id parameters. (up to 3,200 of his/her most recent tweets)
#twitter.statuses.user_timeline(screen_name="billybob")

# Get a sample of the public data following through Twitter
ITERATOR = TWITTER_STREAM.statuses.filter(track="Google", language="en")

# Print each tweet in the stream to the screen
# Here we set it to stop after getting 1000 tweets.
# You don't have to set it to stop, but can continue running
# the Twitter API to collect data for days or even longer.
TWEET_COUNT = 10
for tweet in ITERATOR:
    TWEET_COUNT -= 1
    # Twitter Python Tool wraps the data returned by Twitter
    # as a TwitterDictResponse object.
    # We convert it back to the JSON format to print/score
    print json.dumps(tweet['user']['name'])
    print json.dumps(tweet['user']['screen_name'])
    print json.dumps(tweet['text'])
    print ' '

    # The command below will do pretty printing for JSON data, try it out
    # print json.dumps(tweet, indent=4)

    if TWEET_COUNT <= 0:
        break



def get_recent_tweet_ids_from_file():
    """
    Open and read from TweetID collection file to build a list used to
    set ID limits for timeline scraping.
    """
    my_file = open("TweetID.txt", "r")

    if my_file.mode == 'r':
        file_lines = my_file.readlines()
        player_list = [Player(line.split(",")[0], line.split(",")[1]) for line in file_lines]

    file.close()
    return player_list
