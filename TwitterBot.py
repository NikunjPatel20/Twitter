from flask import Flask, render_template, request, redirect, url_for, flash
import tweepy
import os

app = Flask(__name__)

# Set up Tweepy API
auth = tweepy.OAuthHandler(os.environ.get('api_key'), os.environ.get('api_key_secret'))
auth.set_access_token(os.environ.get('access_token'), os.environ.get('access_token_secret'))
api = tweepy.API(auth)

# Home route
@app.route('/')
def home():
    return render_template('home.html')

# Following route
@app.route('/following')
def show_following():
    name = 'NikunjPatel2029'
    friends = api.get_friends(screen_name=name)
    return render_template('following.html', friends=friends)

# Friend route
@app.route('/friend', methods=['POST'])
def add_friend():
    screen_name = request.form['screen_name']
    api.create_friendship(screen_name=screen_name)
    flash(f'You are now following {screen_name}', 'success')
    return redirect(url_for('home'))

# User ID route
@app.route('/user_id', methods=['POST'])
def get_user_id():
    screen_name = request.form['screen_name']
    user = api.get_user(screen_name=screen_name)
    user_id = user.id
    flash(f'The user ID of {screen_name} is {user_id}', 'info')
    return redirect(url_for('home'))

# Timeline route
@app.route('/timeline')
def show_timeline():
    timeline = api.home_timeline()
    return render_template('timeline.html', timeline=timeline)

# Check Followers route
@app.route('/check_followers')
def show_followers():
    followers = api.get_followers()
    return render_template('followers.html', followers=followers)

# Messages route
@app.route('/messages', methods=['GET', 'POST'])
def send_message():
    if request.method == 'POST':
        screen_name = request.form['screen_name']
        text = request.form['text']
        receipent_id = userId(screen_name=screen_name)
        api.send_direct_message(receipent_id, text)
        flash(f'Message sent to {screen_name}', 'success')
        return redirect(url_for('home'))
    return render_template('messages.html')

if __name__ == '__main__':
    app.run(debug=True)
