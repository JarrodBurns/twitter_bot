import tweepy
from hidden import consumer_key, consumer_secret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

try:
    redirect_url = auth.get_authorization_url()
except tweepy.TweepError:
    print("Error! Failed to get request token.")

print("Follow this link from your bot account.")
print(redirect_url)

verifier = input('Verifier:')

try:
    auth.get_access_token(verifier)
except tweepy.TweepError:
    print("Error! Failed to get access token.")

new_token = auth.access_token
new_secret = auth.access_token_secret

if new_token and new_secret is not None:
    print("These are your keys: token, secret")
    print(new_token)
    print(new_secret)
