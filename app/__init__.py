import os
from flask import Flask, render_template, request
from dotenv import load_dotenv
from peewee import *
import datetime
from playhouse.shortcuts import model_to_dict

load_dotenv()
app = Flask(__name__)

# using peewee function to connect to MYSQL database
if os. getenv ( "TESTING" ) == "true":
    print ("Running in test mode")
    mydb= SqliteDatabase( 'file: memory?mode=memory&cache=shared', uri=True)
else:
    mydb = MySQLDatabase(os.getenv("MYSQL_DATABASE"),
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASSWORD"),
        host=os.getenv("MYSQL_HOST"),
        port=3306)


#mydb = MySQLDatabase(os.getenv("MYSQL_DATABASE"),
 #   user=os.getenv("MYSQL_USER"),
  #  password=os.getenv("MYSQL_PASSWORD"),
   # host=os.getenv("MYSQL_HOST"),
    #port=3306
#)

print(mydb)

# peewee model for Timeline Post 
class TimelinePost(Model):
    name = CharField()
    email = CharField()
    content = TextField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = mydb
    
mydb.connect()
mydb.create_tables([TimelinePost])


# pages routes
@app.route('/')
def index():
    return render_template('workex_ed_caroline.html', title="Caroline Silva", url=os.getenv("URL"))

@app.route('/hobbies')
def hobbies():
    return render_template('hobbies_template.html', title="Hobbies", url=os.getenv("URL"))

@app.route('/projects')
def projects():
    return render_template('projects_template.html', title="Projects", url=os.getenv("URL"))

@app.route('/resume')
def resume():
    return render_template('resume.html', title="Resume", url=os.getenv("URL"))

@app.route('/contact')
def contact():
    return render_template('contact.html', title="Contact", url=os.getenv("URL"))

# timeline POST route
@app.route('/api/timeline_post', methods=['POST'])
def post_time_line_post():
    name = request.form['name']
    email = request.form['email']
    content = request.form['content']
    timeline_post = TimelinePost.create(name=name, email=email, content=content)

    return model_to_dict(timeline_post)

# timeline GET route
@app.route('/api/timeline_post', methods=['GET'])
def get_time_line_post():
    return {
        'timeline_posts' : [
            model_to_dict(p)
            for p in
TimelinePost.select().order_by(TimelinePost.created_at.desc()) 
       ]
    }

# create timeline post page
@app.route('/timeline')
def timeline():
    return render_template('timeline.html', title="Timeline")
