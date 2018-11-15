import numpy as np
from twitter_collect.twitter_connection_setup import *
import pandas as pd
import tweepy
# We import our access keys:
from twitterPredictor.credentials import *
import matplotlib.pyplot as plt


# j'ai dû rajouter les deux programmes suivants car python refusait d'aller les chercher dans d'autres modules ou/et fichiers
# Erreur étrange sachant que les programmes tournent correctement indépendants
def twitter_setup():
    """
    Utility function to setup the Twitter's API
    with an access keys provided in a file credentials.py
    :return: the authentified API
    """
    # Authentication and access using keys:
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    # Return API with authentication:
    api = tweepy.API(auth)
    return api


def collect_to_pandas_dataframe():
    connexion = twitter_setup()
    tweets = connexion.search("@EmmanuelMacron", language="fr", rpp=100)
    data = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['tweet_textual_content'])
    data['len'] = np.array([len(tweet.text) for tweet in tweets])
    data['ID'] = np.array([tweet.id for tweet in tweets])
    data['Date'] = np.array([tweet.created_at for tweet in tweets])
    data['Source'] = np.array([tweet.source for tweet in tweets])
    data['Likes'] = np.array([tweet.favorite_count for tweet in tweets])
    data['RTs'] = np.array([tweet.retweet_count for tweet in tweets])
    return data

#j'ai choisi que si il y a égalité entre deux tweets en termes de Likes ou de RTs on prend juste celui donné par np.max()
def higher_retweet():
    # Find and print the tweet with the higher number of retweets
    data = collect_to_pandas_dataframe()
    rt_max = np.max(data['RTs'])
    rt = data[data.RTs == rt_max].index[0]
    # Max RTs:
    print("The tweet with more retweets is: \n{}".format(data['tweet_textual_content'][rt]))
    print("Number of retweets: {}".format(rt_max))
    print("{} characters.\n".format(data['len'][rt]))


def higher_likes():
    data = collect_to_pandas_dataframe()
    like_max = np.max(data['Likes'])
    like = data[data.Likes == like_max].index[0]
    # Max Likes:
    print("The tweet with more likes is: \n{}".format(data['tweet_textual_content'][like]))
    print("Number of Likes: {}".format(like_max))
    print("{} characters.\n".format(data['len'][like]))


def Who_made_more_Rt(): #détermine à qui appartient le tweet avec le plus de RT
    data = collect_to_pandas_dataframe()
    rt_max = np.max(data['RTs'])
    who = data[data.RTs == rt_max].index[0]
    # User with Max RTs:
    print("The user with more retweets is: \n{}".format(data['tweet_textual_content'][who]))
    print("Number of retweets: {}".format(rt_max))

def graph_Likes_and_RT():
    #trace le graphe de l'évolution des retweets et likes au cours du temps
    data = collect_to_pandas_dataframe()
    tfav = pd.Series(data=data['Likes'].values, index=data['Date'])
    tret = pd.Series(data=data['RTs'].values, index=data['Date'])
    #liste des couples (Date,Nombre de retweets), en réalité c'est une série
    # Likes vs retweets visualization:
    tfav.plot(figsize=(16,4), label="Likes", legend=True) #trace les likes au cours du temps
    tret.plot(figsize=(16,4), label="Retweets", legend=True)
    plt.show()
    #affiche le graphique

def graph_len_tweet():#affiche la taille des tweets au cours du temps
    data = collect_to_pandas_dataframe()
    tlen=pd.Series(data=data['len'].values,index=data['Date'])
    tlen.plot(figsize=(16,10),label='len of tweets', legend=True)
    plt.show()

