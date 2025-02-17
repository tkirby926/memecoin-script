import requests
import tweepy
import time
import random
from tweets import tweets

# Function to post the tweet using Tweepy
def post_tweet(tweet):
    # Set up Twitter API credentials
    access_token = '1888291574972379136-xFuZUCfLS6U24wKOOowjqQUghZ21fh'
    access_token_secret = 'khVcxWigsUFEWtKfzBt0f4hGvlnNJJWQfTE34KiqP4Zn9'
    api_key = 'gvDJ7eyGVZ2GkC85DLTWkNRCf'
    api_key_secret = 'lhpUBVr3xkGDvVeyyPjiSLBtYEs5AxbMkGBYR26ooqZ3i9Na6E'

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
    random.shuffle(tweets)
    counter = 0
    while True and counter < 48:
        post_tweet(tweets[counter])
        counter += 1
        print(counter)
        time.sleep(1800)
    while True: 
        post_tweet(tweets[counter])
        counter += 1
        print(counter)
        time.sleep(7200)
if __name__ == "__main__":
    main()