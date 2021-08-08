from credentials import api_key, api_key_secret, access_token, access_token_secret
import time
import tweepy
import random

auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)

FILE_NAME = 'last_seen.txt'

def read_last_seen(FILE_NAME):
    file_read = open(FILE_NAME, 'r')
    last_seen_id = int(file_read.read().strip())
    file_read.close()
    return last_seen_id

def store_last_seen(FILE_NAME, last_seen_id):
    file_write = open(FILE_NAME, 'w')
    file_write.write(str(last_seen_id))
    file_write.close()
    return

def reply_to_tweets():
    print("Retrieving/replying to tweets...", flush=True)
    last_seen_id = read_last_seen(FILE_NAME)
    mentions = api.mentions_timeline(last_seen_id, tweet_mode = 'extended')
    for mention in reversed(mentions):
        print(str(mention.id) + mention.full_text, flush=True)
        last_seen_id = mention.id
        store_last_seen(FILE_NAME, last_seen_id)
        if '8!' in mention.full_text.lower():
            print('Found correct sytax! (8!)', flush=True)
            print('Responding...')
            responses = ['It is certain.',
                         'It is decidedly so.',
                         'Without a doubt.',
                         'Yes, definitely.',
                         'You may rely on it.',
                         'As I see it, yes.',
                         'Most likely.',
                         'Outlook good.',
                         'Yes.',
                         'Signs point to yes.',
                         'Reply hazy try again.',
                         'Ask again later.',
                         'Better not tell you now.',
                         'Cannot predict now.',
                         'Concentrate and ask again.',
                         "Don't count on it.",
                         'My reply is no.',
                         'My sources say no.',
                         'Outlook not so good.',
                         'Very doubtful.']
            api.update_status('@' + mention.user.screen_name + " " + f'{random.choice(responses)}', mention.id)

while True:
    reply_to_tweets()
    time.sleep(10)