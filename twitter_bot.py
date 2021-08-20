# twitter_bot.py
from hidden import consumer_key, consumer_secret, access_token, access_token_secret, email, password, mail_to
import tweepy
import time
import yagmail
from datetime import datetime


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True,
                 wait_on_rate_limit_notify=True)
FILE_NAME = "last_seen.txt"
subject = "Twitter bot has detected a message."


def send_email(mail_to, subject, content):

    yagmail.SMTP({email: "Twitter Bot"}, password).send(mail_to, subject, content)


def read_last_seen(FILE_NAME):

    file_read = open(FILE_NAME, "r")
    last_seen_id = int(file_read.read().strip())
    file_read.close()
    return last_seen_id

def store_last_seen(FILE_NAME, last_seen_id):

    file_write = open(FILE_NAME, "w")
    file_write.write(str(last_seen_id))
    file_write.close()
    return

def reply():

    tweets = api.mentions_timeline(read_last_seen(FILE_NAME), tweet_mode="extended")
    for tweet in reversed(tweets):
        if "#respondtome" in tweet.full_text.lower():
            api.update_status("@" + tweet.user.screen_name +
                              " Twitter bot reporting in!", tweet.id)  # Reply
            api.retweet(tweet.id)  # Share
        else:
            api.update_status("@" + tweet.user.screen_name +
                              " Jarrod has been forwarded a copy of your message." +
                              " Use #respondtome to have BotJarrod generate more engagement. (60s delay)",
                              tweet.id)
            send_email(mail_to, subject, str(f"Message from: @{tweet.user.screen_name}\n\n{tweet.full_text}"))

        api.create_favorite(tweet.id)  # like
        api.create_friendship(tweet.user.screen_name)  # Sub
        store_last_seen(FILE_NAME, tweet.id)
        print(f"Now following {tweet.user.screen_name}")
        print(str(tweet.id), "-", tweet.full_text)


count = 0

current_time = datetime.now().strftime('%m-%d-%Y @ %H:%M:%S.')

while True:
    reply()
    time.sleep(60)  # 60 is one minute.
    count += 1
    if count % 60 == 0:  # 60 is one hour. 1440 is one day.
        print(f"Connection valid on {current_time} Request ID: {count}")
