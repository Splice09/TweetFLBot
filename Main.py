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
from Player import *

oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

# Initiate the connection to Twitter Streaming API
twitter_stream = TwitterStream(auth=oauth)

#Call function to obtain recent TweetIds from file
PlayerList = GetRecentTweetIdsFromFile()

# Returns a collection of the most recent Tweets posted by the user indicated by the screen_name or user_id parameters. (up to 3,200 of his/her most recent tweets)
#twitter.statuses.user_timeline(screen_name="billybob")

# Get a sample of the public data following through Twitter
iterator = twitter_stream.statuses.filter(track="Google", language="en")

# Print each tweet in the stream to the screen 
# Here we set it to stop after getting 1000 tweets. 
# You don't have to set it to stop, but can continue running 
# the Twitter API to collect data for days or even longer. 
tweet_count = 10
for tweet in iterator:
    tweet_count -= 1
    # Twitter Python Tool wraps the data returned by Twitter 
    # as a TwitterDictResponse object.
    # We convert it back to the JSON format to print/score
    print json.dumps(tweet['user']['name'])
    print json.dumps(tweet['user']['screen_name'])
    print json.dumps(tweet['text'])
    print (' ')  
    
    # The command below will do pretty printing for JSON data, try it out
    # print json.dumps(tweet, indent=4)
       
    if tweet_count <= 0:
        break


def GetRecentTweetIdsFromFile():
    file = open("TweetID.txt", "r")

    if file.mode == 'r':
        fileLines = file.readlines()
        PlayerList = [Player(line.split(",")[0], line.split(",")[1]) for line in fileLines]

    file.close()
    return PlayerList