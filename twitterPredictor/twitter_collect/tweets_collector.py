def collect():
    connexion = twitter_connection_setup.twitter_setup()
    tweets = connexion.search("Emmanuel Macron",language="french",rpp=100)
    for tweet in tweets:
        print(tweet.text)

def collect_by_user(user_id):
    connexion = twitter_connection_setup.twitter_setup()
    statuses = connexion.user_timeline(id = user_id, count = 200)
    for status in statuses:
        print(status.text)
    return statuses

from tweepy.streaming import StreamListener
class StdOutListener(StreamListener):

    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        if  str(status) == "420":
            print(status)
            print("You exceed a limited number of attempts to connect to the streaming API")
            return False
        else:
            return True




def collect_by_streaming():

    connexion = twitter_connection_setup.twitter_setup()
    listener = StdOutListener()
    stream=tweepy.Stream(auth = connexion.auth, listener=listener)
    stream.filter(track=['Emmanuel Macron'])

from twitter_collect import twitter_connection_setup
from tweepy.streaming import StreamListener
import tweepy

def get_candidate_queries(num_candidate, file_path,file_type):
    """
    Generate and return a list of string queries for the search Twitter API from the file file_path_num_candidate.txt
    :param num_candidate: the number of the candidate
    :param file_path: the path to the keyword and hashtag
    files
    :param type: type of the keyword, either "keywords" or "hashtags"
    :return: (list) a list of string queries that can be done to the search API independently
    """
    queries=[]

    keywords_file_path="{}_{}_candidate_{}.txt".format(file_path,file_type,num_candidate)
    try:
        with open(keywords_file_path,'r') as keyword_file:
            keywords=keyword_file.read().split("\n")

        i=0
        for keyword1 in keywords:
            if file_type == "hashtag":
                queries.append("#{}".format(keyword1))
            else:
                queries.append("{}".format(keyword1))
            if i <len(keywords)-2:
                for keyword2 in keywords[i+1:]:
                    if file_type == "hashtag":
                        queries.append("#{} AND #{}".format(keyword2, keyword2))
                    else:
                        queries.append("{} AND {}".format(keyword2, keyword2))
            i = i + 1

        return queries

    except IOError:
        print("file {} is missing.".format(keywords_file_path))
        return []

def collect_user_by_streaming(user_id):
    connexion=twitter_connection_setup.twitter_setup()
    listener=StdOutListener()
    stream=tweepy.Stream(auth=connexion.auth,listener=listener)
    stream.filter(follow=[user_id])
