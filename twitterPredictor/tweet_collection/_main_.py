def Collect(num_candidate):
    connexion=twitter_connection_setup.connection_setup()
    Retweets=collect_tweet_candidate_activity.get_retweets_of_candidate(num_candidate)
    Replies=collect_tweet_candidate_activity.get_replies_to_candidate(num_candidate)
    Tweets=collect_candidate_actuality_tweets.get_tweets_from_candidates_search_queries(tweets_collector.get_candidate_queries(num_candidate ,C:\Users\quent\PycharmProjects\twitterPredictor\CandidateData))

def store_tweets(tweets,filename):
    return None
