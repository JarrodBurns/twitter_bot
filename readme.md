
# Twitter Bot

Twitter Bot, Twitter, API, OAuth, Email, 
This bot will monitor and reply to twitter mentions as well as email a specified account the details of messages.


This bot has the capability to:

- Monitor an account for incoming @mentions
- React to a custom #hashtag
- Retweet, Like, follow and mention
- Email a user to report the contents of messages.

## Version Control

Twitter bot is dependent on the following libraries

- [python](https://docs.python.org/3/) 3.9.6 
- [tweepy](https://docs.tweepy.org/en/stable/install.html) 3.10.0 
- [yagmail](https://yagmail.readthedocs.io/en/latest/setup.html) 0.14.256

## Files

1. hidden.py - Where all of your secret stuff goes.
2. twitter_bot_access.py - How you will get your bots account credentials
3. twitter_bot.py - The script you will need to run continuously.

## hidden.py

### Twitter and OAuth
I have provided an additional file named hidden.py, you will need to use a twitter developer account to acquire access tokens and secrets. You can apply for a developer account (and they will approve almost anyone) at [twitter](https://developer.twitter.com/en/apply-for-access). Once you have your keys type their values in **hidden.py**

    ...
    consumer_key = "hdfjksdhfjhfsdfd"
     
    access_token = "djsfhjksdhfjdsjdkshfjdf"
    ...

### Email and authentication
If you want the bot to email you when you receive a message you will need to set up a gmail account with the option **allow less secure apps ON** This is also very easy to do, just use a burner account.

### Security
If you are concerned about security; you may need to implement more secure means to handle the email traffic as well as the security of your keys/passwords. Use this code at your own risk.

## twitter_bot_access.py

### Bot Access
Once you have your key information filled out in **hidden.py**, access to your developer account, and access to your bot account (you can be signed in to as many as five at one time.) You will need to run **twitter_bot_access.py** in your BASH. 

- Follow the link provided with your bot account
- Enter the validation code in the terminal screen
- If successful you will be provided with your access token/secret.

You should see something like this.

![bot_access_ss](https://user-images.githubusercontent.com/87616660/129512022-9847460e-91f2-4bc5-b2a2-8e438ea9275e.png)

These credentials allow you to post on behalf of another account.

## twitter_bot.py

### Hosting
If it is going to be online all the time it needs somewhere to live. I recommend something like [Python Anywhere](https://www.pythonanywhere.com/user/Xiji/). They have a basic account that will be more than what our bot will require. Also it is 100% **FREE**

## Conclusion
Thanks for taking the time to review the readme, if you have any questions feel free to message my twitter bot, @BotJarrod or my gmail at ta747839@gmail.com
