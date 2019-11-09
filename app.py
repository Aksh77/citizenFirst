from flask import Flask, render_template, request
import os
import requests
from keywordDetail import viewKeywords
import userDetail as user

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
userKeywords = []
username = ''

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        if (request.form['username']):
            username = request.form['username']
        return render_template('keywords.html', keywords=viewKeywords(), username=username)
    return render_template('index.html')

@app.route('/keywords', methods=['GET', 'POST'])
def get_keywords():
    if request.method == "POST":
        keyword = request.form['keyword']
        if (keyword not in userKeywords):
            userKeywords.append(keyword)
    return render_template('keywords.html', keywords=viewKeywords(), userKeywords=userKeywords, username=username)

@app.route('/newsfeed', methods=['GET', 'POST'])
def get_newsfeed():
    if request.method == "POST":
        newUser = user.User(username, userKeywords)
    return render_template('newsfeed.html', username=username)
# 
# @app.route('/cause', methods=['GET', 'POST'])
# def get_cause():
#     return render_template('cause.html', cause=cause)
#
# @app.route('/minister', methods=['GET', 'POST'])
# def get_cause():
#     return render_template('minister.html', name=ministerName)

if __name__ == '__main__':
    app.run()
