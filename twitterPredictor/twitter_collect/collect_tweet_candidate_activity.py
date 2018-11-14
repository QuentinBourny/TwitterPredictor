def get_replies_to_candidate(num_candidate,twitter_api):
    tweets_and_replies=[]
    statuses = twitter_api.user_timeline(id=num_candidate, count="20")
    for status in statuses:
        curr_tweet_replies=[]

        print(status.text)
    return statuses
