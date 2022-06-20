import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('workex_ed_caroline.html', title="MLH Fellow", url=os.getenv("URL"))

@app.route('/hobbies')
def hobbies():
    return render_template('hobbies_template.html', title="Hobbies", url=os.getenv("URL"))

@app.route('/projects')
def projects():
    return render_template('projects.html', title="Projects", url=os.getenv("URL"))
