

#Posting tweet
def post_tweet(api, post_content='', image_path=None):
	try:
		if image_path:
			api.update_with_media(image_path, post_content)
		else:
			api.update_status(post_content)	
	except tweepy.error.TweepError as tweepyError:
		print("Exception: ", tweepyError)


#Formatting the tweet
def format_feed(feed_data=dict()):
	feed_fromat = """
			Title: {0} \n
			\n
			Description: {1} \n
			\n
			Read More: {2}
			""".format(feed_data['post_title'], feed_data['post_description'], feed_data['post_link'])

	return feed_fromat


#Iterating over the list of feeds to post as tweet
def posting_feeds(api, feeds=list()):
	for feed in feeds:
		formatted_tweet = format_feed(feed)
		post_tweet(api, post_content=formatted_tweet)

