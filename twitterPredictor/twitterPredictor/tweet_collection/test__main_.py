from twitter_collect.tweets_collector import collect
from pytest import *


def test_collect():
    tweets = collect()
    data =  transform_to_dataframe(tweets)
    assert 'tweet_textual_content' in data.columns

import pandas as pd

def transform_to_dataframe(tweets):
    tmp_list=[]
    if type(tweets)=='dictionary' or type(tweets)=='list':
        for tweet in tweets:
            tweet_as_dict={"text":tweet.text,"user": tweet.user.id ,"date":str(tweet.created_at),"hashtags":tweet.entities.get("hashtags"),"retweeted":tweet.retweeted,"retweet_count":tweet.retweet_count}
            tmp_list.append(tweet_as_dict)#rajouter condition si liste des hashtags vides ou non
    else:
        tmp_list.append("I'm empty")
    Dataframe=pd.DataFrame(tmp_list)
    return Dataframe

