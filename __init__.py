from flask import Flask
from flask.ext.mongoengine import MongoEngine

app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {'DB': "song_match"}
app.config["SECRET_KEY"] = "secret"

db = MongoEngine(app)

if __name__ == '__main__':
    app.run()
