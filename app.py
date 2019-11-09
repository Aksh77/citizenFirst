from flask import Flask, render_template, request
import os
import requests

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])

@app.route('/', methods=['GET', 'POST'])

def index():
    if request.method == "POST":
        user = request.form['username']
        return render_template('keywords.html', keywords = get_keywords() )
        #return render_template('keywords.html', myFunction = get_keywords(user) )
    return render_template('index.html')

def get_keywords():
    return ['A', 'B', 'C', 'D', 'E']

if __name__ == '__main__':
    app.run()
