import datetime
from flask import url_for
from song_match_api import db

class Song(db.EmbeddedDocument):
    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
    title = db.StringField(max_length=255, required=True)

    meta = {
        'indexes': ['title']
    }

class Match(db.EmbeddedDocument):
    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
    songs = db.ListField(db.EmbeddedDocumentField('Song'))

class User(db.Document):
    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
    name = db.StringField(max_length=255, required=True)
    email = db.StringField(max_length=255, required=True)
    password = db.StringField(max_length=255, required=True)
    matches = db.ListField(db.EmbeddedDocumentField('Match'))
    songs = db.ListField(db.EmbeddedDocumentField('Song'))

    meta = {
        'indexes': ['name', 'email']
    }
