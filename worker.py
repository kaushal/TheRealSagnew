import traceback
import time
import re
import random
from keys import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET
from quotes import quotes, hashtags

from collections import defaultdict
from datetime import datetime, timedelta

#this package seems outdated, but it was super simple to set up
import tweepy

ACCOUNTS = ["sagnewshreds"]

#how often to check for new tweets (careful of twitter rate limiting)
DELAY = 40

#how long until we don't consider a tweet new?
#this is to deal with tweets bizarrely repeating
EXPIRED_TIME = timedelta(minutes=2)

URL_RE = ".+\..+"  # crude, but should handle most of what Sam tweets

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

def send_tweet(message):
    final_message = message
    #add in footers (hashtags and users)
    for footer in FOOTERS:
        if len(final_message + " " + footer) <= 140:
            final_message += " " + footer
    try:
        api.update_status(final_message)
        print "Tweeted:"
        print final_message.encode('utf-8')
    except:
        #this will print to heroku logs
        print "Error sending tweet:"
        print final_message.encode('utf-8')
        traceback.print_exc()


def to_upper(message):
    upper_message = []
    for token in message.split(" "):
        if is_link(token):
            print "%s is a link" % token
            upper_message.append(token)
        else:
            upper_message.append(token.upper())
    return " ".join(upper_message)

def getAtMentions(message):
    finalTokens = '.@sagnewshreds'
    for token in message.split(" "):
        if token[0] == '@' or token[0] == '#':
            finalTokens += ' ' + token
    return finalTokens


def is_link(token):
    return True if re.match(URL_RE, token) else False

if __name__ == "__main__":
    last_tweets = defaultdict(str)  # keep track of last tweet from the stream
    while True:
        for user in ACCOUNTS:
            try:
                #get most recent tweet
                tweet = api.user_timeline(user)[0]
                if tweet.text != last_tweets[user]:
                    last_tweets[user] = tweet.text
                    if(datetime.now() - tweet.created_at < EXPIRED_TIME):
                        FOOTERS = [random.choice(quotes), random.choice(hashtags)]
                        send_tweet(getAtMentions(tweet.text))
                    else:
                        print "Got tweet but it was too old for", user
                        print tweet.text.encode('utf-8')
                else:
                    print "Got same tweet for", user
            except IndexError:
                #no tweeets found for this user
                print "Error getting tweet for", user
                traceback.print_exc()
            finally:
                time.sleep(DELAY)  # Avoid Twitter rate limiting
