__author__ = 'Rizwan Hameed'
__email__ = 'rizwanbutt314@gmail.com'
__date__ = 'March 19, 2018'
"""
	Check out my main scraping projects !
	https://www.youtube.com/playlist?list=PLh2kzLvQxb76sv7s6aUB6378zy4Tkpzv0
"""
import tweepy
import config
import sys
from rss_feeds import nasa_gov
from optparse import OptionParser
from utils import (
    tweet_poster,
    tweet_liker_or_retweet
)


def arguments_maker(arguments):

    parser = OptionParser()

    parser.add_option("-o", "--option",
                      action="store", type="string", dest="option")

    (options, args) = parser.parse_args(arguments)
    return options


# Authenticating api
def authenticate_api():
    # Authentication of Twitter user
    auth = tweepy.OAuthHandler(config._CONSUMER_KEY, config._CONSUMER_SECRET)
    auth.set_access_token(config._ACCESS_TOKEN, config._ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)
    return api


# Posting RSS feeds as tweets
def crawl(option='like'):
    api = authenticate_api()

    # Posting feeds of Nasa Gov site
    if option == 'post':
        nasa_gov_feeds = nasa_gov.main(config._NASA_GOV_URL)
        tweet_poster.posting_feeds(api, feeds=nasa_gov_feeds)
    else:
        # Liking or Retweeting of tweets of followers for a user
        tweet_liker_or_retweet.like_or_retweet(api, config._KEYWORDS_FILE, option=option)

    print("Finished !")


if __name__ == '__main__':
    if len(sys.argv) > 1:
        args = arguments_maker(sys.argv[1:])
        option = args.option
        if option in ['post','like','retweet']:
            crawl(option=option)
        else:
            print("Invalid Option !")
