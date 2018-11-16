import dash
import dash_core_components as dcc
import dash_html_components as html
from textblob import TextBlob
import matplotlib.pyplot as plt

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

def donne_pourcentage_avis_neg(id_nom):
    connexion = twitter_setup()
    tweets = connexion.search(id_nom, language="fr", rpp=100)
    tweets = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['tweet_textual_content'])
    neg_tweets=[]
    for tweet in tweets['tweet_textual_content']:
        texte=TextBlob(tweet)
        #on peut rajouter une traduction mais on est limité ou encore passer par TextBlob-fr
        if texte.sentiment.polarity<-0.00001:
            neg_tweets.append(tweet)
    Percentage_neg=100*len(neg_tweets)/len(tweets['tweet_textual_content'])
    return Percentage_neg

def graph_opinion_tweets_foreign(id_nom,neg_seuil,pos_seuil,language):
    connexion = twitter_setup()
    tweets = connexion.search(id_nom, language="fr", rpp=100)
    tweets = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['tweet_textual_content'])
    pos_tweets=[]
    neu_tweets=[]
    neg_tweets=[]
    for tweet in tweets['tweet_textual_content']:
        texte=TextBlob(tweet)
        """if texte.detect_language()!='en':
            texte=texte.translate(from_lang=language,to='en')"""
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

graph_opinion_tweets_foreign('@xSqueeZie',-0.00001,0.00001,'fr')

external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css']
app=dash.Dash(__name__,external_stylesheets=external_stylesheets)
app.layout=html.Div(children=[html.H1(children='Twitter Monitor'),
                              html.Div(children='''Twitter Monitor : un must de la surveillance'''),
                              dcc.Graph(id='popularity-graph',figure={'data':[{'x':['@EmmanuelMacron',"@MLP_officiel",'@xSqueeZie','@fhollande'],"y":[donne_pourcentage_avis_neg(nom) for nom in ['@EmmanuelMacron',"@MLP_officiel",'@xSqueeZie','@fhollande']],
                                                                               'type':'bar'}],
                                                                      'layout':{'title':'Visualisation des pourcentages des tweets négatifs'}})])
if __name__=='__main__':
    app.run_server(debug=True)



