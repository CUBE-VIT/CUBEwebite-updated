from flask import Flask
from flask_fontawesome import FontAwesome

app = Flask(__name__)
fa = FontAwesome(app)


from flaskblog import routes