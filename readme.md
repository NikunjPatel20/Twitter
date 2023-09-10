# Twitter API Interaction using Tweepy

This project demonstrates how to interact with the Twitter API using Tweepy, a Python library for accessing the Twitter API.

## Setup

1. Clone this repository to your local machine.
2. Obtain API keys and access tokens by creating a Twitter Developer Account and creating an app:
   - Go to the [Twitter Developer Platform](https://developer.twitter.com/en/apps) and create a new app.
   - Obtain the API key, API key secret, Access token, and Access token secret.
3. Configure the API keys and access tokens in a file named `Keys.py`:

```python
# Keys.py

api_key = "YOUR_API_KEY"
api_key_secret = "YOUR_API_KEY_SECRET"
access_token = "YOUR_ACCESS_TOKEN"
access_token_secret = "YOUR_ACCESS_TOKEN_SECRET"

1.Install Tweepy using pip install tweepy.
2.Run the application using python your_script_name.py.

Usage
1.Start by running the Python script that interacts with the Twitter API.
2.The script uses Tweepy to perform various tasks related to Twitter interactions.

Dependencies
-tweepy

Implementation Details
-The script uses Tweepy library to authenticate and interact with the Twitter API.
-It demonstrates functionality such as fetching friends, following users, retrieving user details, fetching the home timeline, checking followers, and sending direct messages.

Notes
-Ensure you have the required API keys and access tokens from Twitter.
-The project assumes you're familiar with creating a Twitter Developer Account and obtaining API keys.
-Remember not to hardcode your API keys directly in the code for security reasons.

Credits
This project was developed by Nikunj Patel.
