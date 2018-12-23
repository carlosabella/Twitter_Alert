import tweepy
import os

consumer_token = os.environ.get('TWITTER_CONSUMER_TOKEN')
consumer_secret = os.environ.get('TWITTER_CONSUMER_KEY')
key = os.environ.get('TWITTER_KEY')
secret = os.environ.get('TWITTER_SECRET')

auth = tweepy.OAuthHandler(consumer_token, consumer_secret)
auth.set_access_token(key, secret)
api = tweepy.API(auth)