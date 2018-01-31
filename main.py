# Imports
import tweepy
from textblob import TextBlob

consumer_key = 'VgRJMO7n5LzCDU92C8e2GwUkr'
consumer_secret = '39erBFJugaQ95wsZt3JNDRkSim9emsWm9muAnU8SezwEFSi4RP'

access_token = '854494782248411137-gzd9QJX5ExFpGAymZLsACDxl809vrj6'
access_token_secret = 'u17xV8aYaYI5I73Lz1dCHPsuuERBk5QsJ7jQ2n1s3UPd6'

# auth variables
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Trump')

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)