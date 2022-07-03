from distutils.command.build_scripts import first_line_re
import email
from pickle import FALSE
from unicodedata import name
import unittest
from venv import create
from peewee import *


from app import TimelinePost

MODELS = [TimelinePost]

test_db = SqliteDatabase(':memory:', pragmas={'foreign_keys': 1})

class TestTimelinePost(unittest.TestCase):
    def setUp(self):
        test_db.bind(MODELS, bind_refs=FALSE, bind_backrefs=FALSE)
        test_db.connect()
        test_db.create_tables(MODELS)
    
    def tearDown(self):
        test_db.drop_tables(MODELS)
        test_db.close()
    
    def test_timeline_post(self):
        first_post = TimelinePost.create( name='John Doe', email='john@example.com', content='Hello world, I\'m John!')
        assert first_post.id == 1
        second_post = TimelinePost.create( name='Jane Doe', email='jane@example.com', content='Hello world, I\'m Jane!')
        assert second_post.id == 2
    def get_timeline_posts():
        
        first_line = TimelinePost.select().get()
        assert first_line == TestTimelinePost.test_timeline_post().first_post
        second_line = TimelinePost.select().get()
        assert second_line == TestTimelinePost.test_timeline_post().second_post