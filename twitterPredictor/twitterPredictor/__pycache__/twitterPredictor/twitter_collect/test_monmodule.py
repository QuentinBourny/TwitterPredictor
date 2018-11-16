from twitter_collect.twitter_connection_setup import *

def test():
    Test=twitter_setup()
    if Test!=None:
        return True
    return False

print(test())
