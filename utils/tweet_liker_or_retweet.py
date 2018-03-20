import tweepy
import pythonLib


# Getting list of a user's followers
def get_user_followers(api):
    print("Getting Followers...")
    users = tweepy.Cursor(api.followers).items()
    followers_list = [user.screen_name for user in users]
    return followers_list


# Liking a tweet using its id
def like_tweet(api, tweet_id):
    try:
        api.create_favorite(tweet_id)
    except tweepy.error.TweepError as tweepyError:
        print("Exception: ", tweepyError)


# Retweet a tweet using its id
def retweet_tweet(api, tweet_id):
    try:
        api.retweet(tweet_id)
    except tweepy.error.TweepError as tweepyError:
        print("Exception: ", tweepyError)


# Processing tweets on the basis of keywords list
def process_tweets(tweets, _KEYWORDS_FILE):
    print("Filtering extracted tweets using given keywords...")
    tweets_ids = list()
    keywords = pythonLib.read_txt_file(_KEYWORDS_FILE)
    for tweet in tweets:
        if any(word in tweet.text for word in keywords): tweets_ids.append(tweet.id)

    return tweets_ids


# Getting tweets of a follower
def follower_tweets(api, follower, option, _KEYWORDS_FILE):
    print("Follower: {0}".format(follower))
    print("Extracting follower's top 100 tweets...")
    tweets = api.user_timeline(screen_name=follower, count=2, include_rts=True)
    tweets_ids = process_tweets(tweets, _KEYWORDS_FILE)
    print("Total Filtered Tweets: {0}".format(str(len(tweets_ids))))
    for tweet_id in tweets_ids:
        if option == 'like':
            print("Liking tweets...")
            like_tweet(api, tweet_id)
        elif option == 'retweet':
            print("Retweeting tweets...")
            retweet_tweet(api, tweet_id)


# Tweets liking process
def like_or_retweet(api, _KEYWORDS_FILE, option='like'):
    followers_list = get_user_followers(api)
    print("Total Followers: {0}".format(str(len(followers_list))))
    for follower in followers_list:
        if follower: follower_tweets(api, follower, option, _KEYWORDS_FILE)
