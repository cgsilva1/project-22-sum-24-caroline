import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"))

@app.route('/user1')
def user1():
    return render_template('userPage1.html', title="Carolines Info", url=os.getenv("URL"))

@app.route('/<user2>')
def user2(user2):
    return render_template('userPage2.html', title="Sree Info", url=os.getenv("URL"))