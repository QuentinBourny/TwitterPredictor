def Collect(num_candidate):
    connexion=twitter_collect.twitter_connection_setup.twitter_setup()
    Retweets=twitter_collect.collect_tweet_candidate_activity.get_retweets_of_candidate(num_candidate) #créer une liste des retweets associés au candidat
    Replies=twitter_collect.collect_tweet_candidate_activity.get_replies_to_candidate(num_candidate) #créer une liste des réponses associées au candidat
    Tweets=twitter_collect.collect_candidate_actuality_tweets.get_tweets_from_candidates_search_queries(tweeter_collect.get_candidate_queries(num_candidate )) #créer la liste des tweets qui correspondent aux hashtags et mots-clés transmis dans deux fichiers texte par l'équipe du candidat
    #si on souhaite avoir une liste de tout ce qui se rapporte au candidat il suffit de rajouter une liste qui correspond à la concaténation des 3 autres
#modifier les noms et prendre aussi les valeurs des likes (voir exemple Fonctionnalité 5)
    return Retweets + Replies + Tweets

import json
def store_tweets(tweets,filename):
    tmp_list=[]
    for tweet in tweets:
        tweet_as_dict={"text":tweet.text,"user": tweet.user.id ,"date":str(tweet.created_at),"hashtags":tweet.entities.get("hashtags"),"retweeted":tweet.retweeted,"retweet_count":tweet.retweet_count}
        tmp_list.append(tweet_as_dict)
    json.dump(tmp_list,filename)
    return tmp_list #modification que permet de travailler dans la fonction create_dataframe ci-dessous

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pytest

def create_dataframe(Status):
    Dataframe=pd.DataFrame(Status)
    return Dataframe
import twitter_collect.tweets_collector


def collect_to_pandas_dataframe():
    connexion = twitter_collect.twitter_connection_setup.twitter_setup()
    tweets = connexion.search("@EmmanuelMacron",language="fr",rpp=100)
    data = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['tweet_textual_content'])
    data['len']  = np.array([len(tweet.text) for tweet in tweets])
    data['ID']= np.array([tweet.id for tweet in tweets])
    data['Date'] = np.array([tweet.created_at for tweet in tweets])
    data['Source'] = np.array([tweet.source for tweet in tweets])
    data['Likes']  = np.array([tweet.favorite_count for tweet in tweets])
    data['RTs']    = np.array([tweet.retweet_count for tweet in tweets])
    return data

with open('blabla.txt','w') as file:
    print(create_dataframe(collect_to_pandas_dataframe()))

