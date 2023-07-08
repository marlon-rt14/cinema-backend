from flask import Flask
from flask_cors import CORS
from config import DATABASE_CONNECTION_URI
from router.router import router

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_CONNECTION_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

@app.route('/')
def hello():
    return 'Hello World!'

app.register_blueprint(router, url_prefix='/api')