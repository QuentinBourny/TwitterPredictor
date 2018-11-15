def Collect(num_candidate):
    connexion=twitter_collect.twitter_connection_setup.twitter_setup()
    Retweets=twitter_collect.collect_tweet_candidate_activity.get_retweets_of_candidate(num_candidate) #créer une liste des retweets associés au candidat
    Replies=twitter_collect.collect_tweet_candidate_activity.get_replies_to_candidate(num_candidate) #créer une liste des réponses associées au candidat
    Tweets=twitter_collect.collect_candidate_actuality_tweets.get_tweets_from_candidates_search_queries(tweeter_collect.get_candidate_queries(num_candidate )) #créer la liste des tweets qui correspondent aux hashtags et mots-clés transmis dans deux fichiers texte par l'équipe du candidat
    #si on souhaite avoir une liste de tout ce qui se rapporte au candidat il suffit de rajouter une liste qui correspond à la concaténation des 3 autres

import json
def store_tweets(tweets,filename):
    tmp_list=[]
    for tweet in tweets:
        tweet_as_dict={"text":tweet.text,"user": tweet.user.id ,"date":str(tweet.created_at),"hashtags":tweet.entities.get("hashtags"),"retweeted":tweet.retweeted,"retweet_count":tweet.retweet_count}
        tmp_list.append(tweet_as_dict)#rajouter condition si liste des hashtags vides ou non
    json.dump(tmp_list,filename)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pytest

def create_dataframe(Status):
    Dataframe=pd.DataFrame(Status)
    return Dataframe
import twitter_collect.tweets_collector
with open('blabla.txt','w') as file:
    store_tweets(twitter_collect.tweets_collector.collect_by_user("@EmmanuelMacron"),file)
    print(create_dataframe(twitter_collect.tweets_collector.collect_by_user("@EmmanuelMacron")))#prendre dans le status(...)
