from dotenv import load_dotenv
from os import getenv

load_dotenv()
MYSQL_USERNAME = getenv("MYSQL_USERNAME")
MYSQL_PASSWORD = getenv("MYSQL_PASSWORD")
MYSQL_DATABASE = getenv("MYSQL_DATABASE")
MYSQL_HOSTNAME = getenv("MYSQL_HOSTNAME")
MYSQL_PORT = getenv("MYSQL_PORT")

DATABASE_CONNECTION_URI = f'mysql://{MYSQL_USERNAME}:{MYSQL_PASSWORD}@{MYSQL_HOSTNAME}:{MYSQL_PORT}/{MYSQL_DATABASE}'

class Config():
    SECRET_KEY = getenv("SECRET_KEY")
    
class DevelpmentConfig(Config):
    DEBUG = True
    HOST = '0.0.0.0'
    PORT = 5000
    
config = {
    "development": DevelpmentConfig
}
