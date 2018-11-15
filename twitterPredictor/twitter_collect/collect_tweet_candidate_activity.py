import tweepy
import twitter_connection_setup

def get_replies_to_candidate(num_candidate):
   #On veut obtenir toutes les réponses associées à un candidat
   connexion=twitter_connection_setup.twitter_setup()
   replies=[] #liste initialisée qui contiendra les réponses
   #récupère les messages récents du candidat
   statuses = connexion.user_timeline(id = num_candidate, language="fr",rpp=100)
   for full_tweet in statuses:

      #requête pour retrouver des tweets repondant a l'utilisateur num_candidate

       query = 'to:'+ str(num_candidate)
       print (full_tweet.text)
       for tweet in connexion.search(q=query, since_id=992433028155654144, result_type='recent',timeout=999999):

           #si le tweet renvoyé par la requête possède un champs "in reply_to__status_id_str" ie si il s'agit d'une réponse à un tweet

          if hasattr(tweet, 'in_reply_to_status_id_str'):
               # si c'est une réponse au tweet actuel (full_tweet) du candidat
              if (tweet.in_reply_to_status_id_str==full_tweet.id_str):
                  replies.append(tweet.text)
                  print(tweet.text)

def get_retweets_of_candidate(num_candidate):
   connexion=twitter_connection_setup.twitter_setup()
   retweet=[]
   #récupère les messages récents du candidat
   statuses = connexion.user_timeline(id = num_candidate, language="fr",rpp=100)
   for full_tweet in statuses:

      #requête pour retrouver des tweets répondant à l'utilisateur num_candidate

       query = 'to:'+str(num_candidate)
       print (full_tweet.text)
       for tweet in connexion.search(q=query, since_id=992433028155654144, result_type='recent',timeout=999999):

          if hasattr(tweet, 'retweeted_status'):
               if (tweet.retweeted_status_id_str==full_tweet.id_str):
                   retweet.append(tweet.text)
                   print(tweet.text)
