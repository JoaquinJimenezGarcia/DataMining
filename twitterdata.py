import tweepy

# IMPORT YOUR OWN CREDENTIALS BY REGISTERING AN APP
# IN https://apps.twitter.com/
consumer_key = "YOUR_CONSUMER_KEY"
consumer_secret = "YOUR_CONSUMER_SECRET"

auth = tweepy.OAuthHandler(consumer_key = consumer_key, consumer_secret = consumer_secret)
api = tweepy.API(auth)

results = []
numberOfTweets = 0

# Search 100 items which contain "DeathStar"
for tweet in tweepy.Cursor(api.search, q="DeathStar").items(100):
    results.append(tweet)

def print_tweet(tweet):
    print ("@" + tweet.author.screen_name)
    print (tweet.text)

for i in range(len(results)):
    print(f"Result nº{i}")
    tweet = results[i]
    print_tweet(tweet)
    numberOfTweets = numberOfTweets + 1

if (numberOfTweets == 0):
    print("There wasn't any tweet.")