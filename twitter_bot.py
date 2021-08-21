
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

hastag = "#respondtome"
hashtag_message = "Twitter bot reporting in!"
no_hashtag_message = ("Jarrod has been forwarded a copy of your message. "
                      "Use #respondtome to have BotJarrod generate more "
                      "engagement. (60s delay)")

subject = "Twitter bot has detected a message."


def send_email(mail_to: str, subject: str, content: str):
    """
    Sends an email to the specified account (mail_to) with
    a specified message (content).
    """
    yagmail.SMTP({email: "Twitter Bot"}, password).send(mail_to, subject, content)


def read_last_seen(FILE_NAME: str):
    """
    Checks the ID of the last seen comment.
    """
    file_read = open(FILE_NAME, "r")
    last_seen_id = int(file_read.read().strip())
    file_read.close()
    return last_seen_id


def store_last_seen(FILE_NAME: str, last_seen_id: str):
    """
    Saves the ID of the last seen comment.
    """
    file_write = open(FILE_NAME, "w")
    file_write.write(str(last_seen_id))
    file_write.close()
    return


def reply(hastag: str):
    """
    Looks for messages, checks for a specified hashtag and replys to users
    """
    tweets = api.mentions_timeline(read_last_seen(FILE_NAME), tweet_mode="extended")

    for tweet in reversed(tweets):

        content = f"Message from: @{tweet.user.screen_name}\n\n{tweet.full_text}"

        if hastag in tweet.full_text.lower():
            # Reply
            api.update_status(f"@{tweet.user.screen_name} {hashtag_message}", tweet.id)
            # Share
            api.retweet(tweet.id)
        else:
            # Reply
            api.update_status(f"@{tweet.user.screen_name} {no_hashtag_message}", tweet.id)
            send_email(mail_to, subject, content)

        api.create_favorite(tweet.id)  # like
        api.create_friendship(tweet.user.screen_name)  # Sub
        store_last_seen(FILE_NAME, tweet.id)
        print(f"---Now following {tweet.user.screen_name}")
        print(f"{tweet.id} - {tweet.full_text}\n")


def current_time() -> str:
    """
    Returns the current time in the following format:
    "m-d-Y @ H:M:S"
    """
    return datetime.now().strftime('%m-%d-%Y @ %H:%M:%S')


print(f"Initializing on {current_time()}.\n")

count = 0
while True:
    reply(hastag)
    time.sleep(60)  # 60 is one minute.
    count += 1
    if count % 60 == 0:  # 60 is one hour. 1440 is one day.
        print(f"Connection valid on {current_time()}. Request ID: {count} Report ID: {int(count / 60)}\n")
