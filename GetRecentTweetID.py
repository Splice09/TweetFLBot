"""
Secondary task executed to collect the most recent Tweet IDs
from specified accounts. Writes those IDs to CSV file for later
consumption.
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

O_AUTH = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

# Initiate the connection to Twitter REST API
TWITTER = Twitter(auth=O_AUTH)

# Returns a collection of the most recent Tweets posted by the user
# indicated by the screen_name or user_id parameters excluding replies.
ITERATOR = TWITTER.statuses.user_timeline(screen_name="JayTrain23", exclude_replies="true")

#Open file we will write tweet ID to
MY_FILE = open("TweetID.txt", "w+")

# Print the first tweet in the returned list to the screen
TWEET_COUNT = 1
for tweet in ITERATOR:
    TWEET_COUNT -= 1
    # Twitter Python Tool wraps the data returned by Twitter
    # as a TwitterDictResponse object.
    # We convert it back to the JSON format to print/score
    MY_FILE.write(tweet['user']['screen_name'] +","+ json.dumps(tweet['id']) + "\r\n")
    print "Tweet ID fetch complete."
    print ''

    if TWEET_COUNT <= 0:
        break


MY_FILE.close()
