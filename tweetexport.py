import tweepy
import pandas as pd
import csv

consumer_key = '**********************'
consumer_secret = '**********************'
access_token = '**********************'
access_token_secret = '**********************'
# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit = True)


df = pd.DataFrame(columns=['text', 'source', 'url'])
msgs = []
msg =[]

for tweet in tweepy.Cursor(api.search, q='#MissionShakti', len="en", rpp=100).items(80):
    msg = [tweet.text, tweet.source, tweet.source_url] 
    msg = tuple(msg)                    
    msgs.append(msg)

df = pd.DataFrame(msgs, columns=['Tweet', 'Source', 'URL'])
print(df.head())

df = df['Tweet']

df.to_csv('mission.csv', index= False, header=False)

