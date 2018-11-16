#même problème que dans Info_Extract
# Twitter App access keys for @user

# Consume:
CONSUMER_KEY    = 'COHRsvSdhEOx6VywsJlM3l1vn'
CONSUMER_SECRET = 'sVMxesPOBn6v95M407yG79kLhhzfGabQ4fBoC2CIe1VJnrwb1I'

# Access:
ACCESS_TOKEN  = '1062338951594287106-3ptwNxvF0Nqb9brBkQONY2tttSAtvL'
ACCESS_SECRET = 'fbtqxKfvGMLNtZqBTr9YB4Ouw0KUCTQzP7MQDMnBtIO4h'
from IPython.display import display
import tweepy
import numpy as np
import pandas as pd

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


def collect_to_pandas_dataframe(id_name="@_OlivierGiroud_"):
    connexion = twitter_setup()
    tweets = connexion.search(id_name, language="fr", rpp=100)
    data = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['tweet_textual_content'])
    data['len'] = np.array([len(tweet.text) for tweet in tweets])
    data['ID'] = np.array([tweet.id for tweet in tweets])
    data['Date'] = np.array([tweet.created_at for tweet in tweets])
    data['Source'] = np.array([tweet.source for tweet in tweets])
    data['Likes'] = np.array([tweet.favorite_count for tweet in tweets])
    data['RTs'] = np.array([tweet.retweet_count for tweet in tweets])
    return data



from textblob import TextBlob
def extract_voc(tweets):
    #extrait le vocabulaire d'un ensemble de tweets
    List_Words=[]
    for tweet in tweets:
        wiki=TextBlob(tweet['tweet_textual_content'])
        for word in wiki.words:
            if word not in List_Words:
                List_Words.append(word)
    return List_Words
from stop_words import get_stop_words

def extract_voc_non_frequent(tweets):
    list_words=extract_voc(tweets)
    frequent_words=get_stop_words('fr')
    #si on suppose n'avoir que des tweets français, une autre possibilité serait de stocker la langue obtenue par la commande
    #TextBlob("tweet['text']).detect_language() et modifier si la langue change la liste des mots fréquents
    list_words_not_frequent=[]
    for word in list_words:
        if word not in frequent_words:
            list_words_not_frequent.append(word)
    return list_words_not_frequent

def opinion_analysis(tweets,neg_seuil,pos_seuil):
    print(tweets)
    pos_tweets=[]
    neu_tweets=[]
    neg_tweets=[]
    for tweet in tweets['tweet_textual_content']:
        texte=TextBlob(tweet)
        print(texte.sentiment.polarity)
        if texte.sentiment.polarity>pos_seuil:
            pos_tweets.append(tweet)
        elif texte.sentiment.polarity<neg_seuil:
            neg_tweets.append(tweet)
        else:
            neu_tweets.append(tweet)
    print("Percentage of positive tweets : {}%".format(len(pos_tweets)*100/len(tweets['tweet_textual_content'])))
    print("Percentage of negative tweets : {}%".format(len(neg_tweets)*100/len(tweets['tweet_textual_content'])))
    print("Percentage of neutral tweets : {}%".format(len(neu_tweets)*100/len(tweets['tweet_textual_content'])))
    #modification de syntaxe possible si tweets n'est pas au format d'une liste de tweets


data=collect_to_pandas_dataframe()
import seaborn as sns
import matplotlib.pyplot as plt
import dash

def graph_opinion_tweets(tweets,neg_seuil,pos_seuil):
    pos_tweets=[]
    neu_tweets=[]
    neg_tweets=[]
    for tweet in tweets['tweet_textual_content']:
        texte=TextBlob(tweet)
        if texte.sentiment.polarity>pos_seuil:
            pos_tweets.append(tweet)
        elif texte.sentiment.polarity<neg_seuil:
            neg_tweets.append(tweet)
        else:
            neu_tweets.append(tweet)
    Percentage_neg=100*len(neg_tweets)/len(tweets['tweet_textual_content'])
    Percentage_neu=100*len(neu_tweets)/len(tweets['tweet_textual_content'])
    Percentage_pos=100*len(pos_tweets)/len(tweets['tweet_textual_content'])
    opinion=['negative tweets','neutral tweets','positive tweets']
    percentages=[Percentage_neg,Percentage_neu,Percentage_pos]
    plt.figure(1,figsize=(9,6))
    plt.subplot(121)
    plt.bar(opinion,percentages)
    plt.subplot(122)
    plt.scatter(opinion,percentages)
    plt.xlabel('Opinion')
    plt.ylabel('Percentage of tweets : %')
    plt.show()


def graph_opinion_tweets_foreign(tweets,neg_seuil,pos_seuil,language):
    pos_tweets=[]
    neu_tweets=[]
    neg_tweets=[]
    for tweet in tweets['tweet_textual_content']:
        texte=TextBlob(tweet)
        """if texte.detect_language()!='en':
            texte=texte.translate(from_lang=language,to='en')"""
        print(texte)
        if texte.sentiment.polarity>pos_seuil:
            pos_tweets.append(tweet)
        elif texte.sentiment.polarity<neg_seuil:
            neg_tweets.append(tweet)
        else:
            neu_tweets.append(tweet)
    Percentage_neg=100*len(neg_tweets)/len(tweets['tweet_textual_content'])
    Percentage_neu=100*len(neu_tweets)/len(tweets['tweet_textual_content'])
    Percentage_pos=100*len(pos_tweets)/len(tweets['tweet_textual_content'])
    opinion=['negative tweets','neutral tweets','positive tweets']
    percentages=[Percentage_neg,Percentage_neu,Percentage_pos]
    plt.figure(1,figsize=(9,6))
    plt.subplot(121)
    plt.bar(opinion,percentages)
    plt.xlabel('Opinion')
    plt.ylabel('Percentage of tweets : %')
    plt.subplot(122)
    plt.scatter(opinion,percentages)
    plt.xlabel('Opinion')
    plt.ylabel('Percentage of tweets : %')
    plt.show()

def donne_pourcentage_avis_neg(id_nom):
    connexion = twitter_setup()
    tweets = connexion.search(id_nom, language="fr", rpp=100)
    tweets = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['tweet_textual_content'])
    neg_tweets=[]
    for tweet in tweets['tweet_textual_content']:
        texte=TextBlob(tweet)
        """if texte.detect_language()!='en':
            texte=texte.translate(from_lang=language,to='en')"""
        if texte.sentiment.polarity<-0.05:
            neg_tweets.append(tweet)
    Percentage_neg=100*len(neg_tweets)/len(tweets['tweet_textual_content'])
    return Percentage_neg

graph_opinion_tweets_foreign(data,-0.05,0.05,'fr')
