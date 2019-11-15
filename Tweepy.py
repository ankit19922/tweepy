import tweepy
from textblob import TextBlob
import pandas as pd
import os
tweetlist=[]
tweet_type=[]

Access_token = "1088749854774517760-cRbYAgEMeUeuwhVR6s8oHaXrKBRh32"
Access_token_secret = "llBKfHQqgKEM1WqAadrLjYuuNFJIS3sgDElwiHTRXLRs3"
Consumer_key = "EazL5W6t9GOMpZj243UEEKyvI"
Consumer_secret_key = "SSP33bWsIyQTRA17Lnb36oBL8YoWbZbJfYjGWmtQxTpP4XqtxO"

auth = tweepy.OAuthHandler(Consumer_key, Consumer_secret_key)


auth.set_access_token(Access_token, Access_token_secret)

api = tweepy.API(auth,wait_on_rate_limit=True)

tweets=tweepy.Cursor(api.search,q="Brexit",lang='en', since='2018-01-01').items(100000)

for tweet in tweets:
    tweetlist.append(tweet.text)
    print(tweet.text)
df=pd.DataFrame(tweetlist)
#print(df)
df.to_csv('D:/data.csv')


