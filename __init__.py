from flask import Flask
from flask.ext.mongoengine import MongoEngine
import os

app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {'DB': "song_match"}
app.config["SECRET_KEY"] = os.getenv('SECRET_KEY')

db = MongoEngine(app)

if __name__ == '__main__':
    app.run()
