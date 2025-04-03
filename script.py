import requests
import tweepy
import time
import random
from tweets import tweets

# Function to post the tweet using Tweepy
def post_tweet(tweet):
    # Set up Twitter API credentials
    access_token = '1906370268164984832-LWG5N3gxZolcxVBMGIhouBBLLYqMmN'
    access_token_secret = 'YDIMNJoz9wfJVDELGBME490vsK3UhiYCk6Nkxo8UpPr5C'
    api_key = 'gcGp1y9vV7i8VZFYhR2ylJP7H'
    api_key_secret = '8p2sTjfDdKo7FTXApWRkw9aW6jQ7zqx1ExOQ87wdtdedjgl3Fk'

    # Authenticate to Twitter
    client = tweepy.Client(
        consumer_key=api_key,
        consumer_secret=api_key_secret,
        access_token=access_token,
        access_token_secret=access_token_secret
    )   
    # Post tweet
    try:
        client.create_tweet(text=tweet)
        print("Tweet posted successfully!")
    except tweepy.TweepyException as e:
        print(f"Error posting tweet: {e}")

# Main loop to run the bot
def main():
    counter = 0
    while True:
            post_tweet(tweets[counter])
            counter += 1
            print(counter)
            if counter < 16:
                time.sleep(1800)  # Sleep for 1800 seconds (30 minutes)
            else:
                time.sleep(10800)
            if counter >= len(tweets):
                counter = 0
if __name__ == "__main__":
    main()