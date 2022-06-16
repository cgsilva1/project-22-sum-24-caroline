import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('workex_ed_caroline.html', title="MLH Fellow", url=os.getenv("URL"))


@app.route('/caroline_hobbies')
def caroline_hobbies():
    return render_template('hobbies_template_caroline.html', title="Caroline's Hobbies", url=os.getenv("URL"))
