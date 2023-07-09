from dotenv import load_dotenv
from os import getenv

if(not getenv("MYSQL_PASSWORD") or not getenv("MYSQL_DATABASE")or not getenv("MYSQL_PORT")):
    load_dotenv()

MYSQL_USERNAME = 'root'
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
    PORT = getenv("SERVER_LOCAL_PORT")
    
config = {
    "development": DevelpmentConfig
}
