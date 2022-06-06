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
    return render_template('workex_ed_caroline.html', title="Carolines Info", url=os.getenv("URL"))

@app.route('/user2')
def user2():
    return render_template('workex_ed_sree.html', title="Sree Info", url=os.getenv("URL"))

@app.route('/caroline_hobbies')
def caroline_hobbies():
    return render_template('hobbies_template_caroline.html', title="Caroline's Hobbies", url=os.getenv("URL"))

@app.route('/sree_hobbies')
def sree_hobbies():
    return render_template('hobbies_template_sree.html', title="sree's Hobbies", url=os.getenv("URL"))
