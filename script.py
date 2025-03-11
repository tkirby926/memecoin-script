import requests
import tweepy
import time
import random
from tweets import tweets

# Function to post the tweet using Tweepy
def post_tweet(tweet):
    # Set up Twitter API credentials
    access_token = '1899564710439325696-5id67NTXrfjLbJDL8Mzt2XIukpYPyZ'
    access_token_secret = 'THyzOWZ2zgOjPOqSmhIwi1XNJpjLsjqukBCwHNXBkgbaX'
    api_key = 'G980ADBBveyNlybTiacvxD5uY'
    api_key_secret = 'u5RoRH08ymdsyVTJpyq3Ln2xo5sF9eT3yKY3gDeRNjdwlgmBuO'

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