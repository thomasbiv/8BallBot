# 8BallBot
*Magic 8 Ball twitter bot*


8BallBot is a simple bot that answers yes or no questions from Twitter users that mention it.
This is a personal project of mine to get a brief introduction to the Twitter API.

### NOTE:

The following instructions are with Windows machines in mind, but the process is mostly consistant across all systems. For installation commands specific to your operating system, please visit the documentation links that will be provided in the instructions below.

## Setup and Installation

### Python

8BallBot is written entirely in Python, so you must have the latest version of Python3 installed. Follow the link below to access the download page:
* [Python3](https://www.python.org/downloads/)

### Libraries

Once Python3 is installed, the proper library to run the bot must be installed as well. For the next install, open your command window by again typing ```cmd``` in the Windows search bar. 

Tweepy is the library that will be used to access the Twitter API. Type or copy/paste this line into the command window:

```
pip install tweepy
```

For a more customized experience or for additional help, the full Tweepy documentation can be found [here.](https://docs.tweepy.org/en/stable/index.html)

## Keys and Tokens

After all installs are completed, the connection between your bot and the Twitter API can be made. All bots have 4 specific keys/tokens that are generated after creating a bot through the twitter developer portal. These keys/tokens are as follows:
* API Key
* API Key Secret
* Access Token
* Access Token Secret

### IMPORTANT NOTE:

These keys/tokens are extremely important and should only be known by you. Do **NOT** upload your keys/tokens to any website for any reason or give your token to anyone you do not trust with the utmost certainty. When someone has access to your keys/tokens, they also have access to your bot which means it is possible for them to use your bot with malicious intent. This could result in your accounts being permanently banned from Twitter.

Enter your keys/tokens **EXACTLY** as they appear on the Twitter developer website into the 'credentials.py' file present in this repository (including single quotes).

After this is completed, 8BallBot should be fully operational on the account the bot has been linked to. Run the bot, and enjoy!

## How To Use:

After running the main file, 8BallBot will periodically scan its Twitter account for valid mentions containing the correct prefix.
The prefix for mentioning 8BallBot is: ```8!```.

### Examples:
*(Note: This is an example. The Twitter handle will vary depending on what handle you have sent for your bot's account.)*

Incorrect Syntax:
* ```@real_8ball Will I win a million dollars?```
* ```@real_8ball !8 Will I win a million dollars?```

Correct Syntax:
* ```@real_8ball 8! Will I win a million dollars?```
* ```@real_ball Will I win a million dollars? 8!```


This project was meant as a small introduction to get myself familiar with Tweepy and the Twitter API, therefore I do not plan to make many updates in the future. If you have any questions or suggestions feel free to message me on Twitter:

---------------------------

Thomas Bivins

[@thomasbiv](https://twitter.com/thomasbiv)

USF Computer Engineering

---------------------------
