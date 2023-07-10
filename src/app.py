from flask import Flask
from flask_cors import CORS
from config import DATABASE_CONNECTION_URI
from router.router import router
import pymysql

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_CONNECTION_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

def check_database_connection():
    try:
        connection = pymysql.connect(
            host=DATABASE_CONNECTION_URI
        )
        connection.close()
        return True
    except Exception as e:
        return False

@app.route('/')
def health_check():
    if check_database_connection():
        return 'OK', 200
    else:
        return 'Database Connection Failed', 500

app.register_blueprint(router, url_prefix='/api')