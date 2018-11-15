def Collect(num_candidate):
    connexion=twitter_collect.twitter_connection_setup.twitter_setup()
    Retweets=twitter_collect.collect_tweet_candidate_activity.get_retweets_of_candidate(num_candidate) #créer une liste des retweets associés au candidat
    Replies=twitter_collect.collect_tweet_candidate_activity.get_replies_to_candidate(num_candidate) #créer une liste des réponses associées au candidat
    Tweets=twitter_collect.collect_candidate_actuality_tweets.get_tweets_from_candidates_search_queries(tweeter_collect.get_candidate_queries(num_candidate ,C:\Users\vince\PycharmProjects\twitterPredictor\CandidateData)) #créer la liste des tweets qui correspondent aux hashtags et mots-clés transmis dans deux fichiers texte par l'équipe du candidat
    #si on souhaite avoir une liste de tout ce qui se rapporte au candidat il suffit de rajouter une liste qui correspond à la concaténation des 3 autres

def store_tweets(tweets,filename):
    tmp_list=[]
    for tweet in tweets:
        tweet_as_dict={"text":tweet.text,"user":tweet.user.id ,"date":tweet.created_at,"hashtags":[hashtag[0]["text"] for hashtag in tweet.entities.hashtags],"retweeted":tweet.retweeted,"retweet_count":tweet.retweet_count}
        tmp_list.append(tweet_as_dict)
    json.dump(tmp_list,filename)
