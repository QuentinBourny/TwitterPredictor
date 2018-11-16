
from textblob import TextBlob
def extract_voc(tweets):
    #extrait le vocabulaire d'un ensemble de tweets
    List_Words=[]
    for tweet in tweets:
        wiki=TextBlob(tweet['text'])
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
    pos_tweets=[]
    neu_tweets=[]
    neg_tweets=[]
    for tweet in tweets:
        texte=Textblob(tweet['text'])
        if texte.sentiment.polarity>pos_seuil:
            pos_tweets.append(tweet)
        elif texte.sentiment.polarity<neg_seuil:
            neg_tweets.append(tweet)
        else:
            neu_tweets.append(tweet)
    print("Percentage of positive tweets : {}%".format(len(pos_tweets)*100/len(tweets)))
    print("Percentage of negative tweets : {}%".format(len(neg_tweets)*100/len(tweets)))
    print("Percentage of neutral tweets : {}%".format(len(neu_tweets)*100/len(tweets)))
#modification de syntaxe possible si tweets n'est pas au format d'une liste de tweets
