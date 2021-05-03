"""
User class created to maintain a list of objects in the main
script.
"""
class User:
    """
    Constructor
    """
    def __init__(self, twitter_screen_name, tweet_id):
        self.tsn = twitter_screen_name
        self.tid = tweet_id
        