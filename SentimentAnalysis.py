# Import sentiment analysis library
from textblob import TextBlob


def get_sentiment_analysis(tweet_string):
    """
    Pass string to sentament analysis function and return double value
    """
    tweet_text_blob = TextBlob(tweet_string)
    sentiment = tweet_text_blob.sentiment
    # Sentiment(polarity=0.39166666666666666, subjectivity=0.4357142857142857)
    sentiment_polarity = tweet_text_blob.sentiment.polarity
    #0.39166666666666666
    return sentiment_polarity
