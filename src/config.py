from dotenv import load_dotenv
from os import getenv, path

if (
    not getenv("MYSQL_PASSWORD")
    or not getenv("MYSQL_DATABASE")
    or not getenv("MYSQL_LOCAL_PORT")
):
    print("Loading environment variables from Dockerfile manually...")
    # Las variables de entorno de Dockerfile, internamente en el proyecto crea un archivo .env, y es la ruta de ese archivo que se carga aqui. 
    path_to_dotenv = path.join('\\'.join(path.dirname(__file__).split('\\')[:-1]), '.env')
    load_dotenv(dotenv_path=path_to_dotenv)

MYSQL_USERNAME = "root"

MYSQL_PASSWORD = getenv("MYSQL_PASSWORD")
MYSQL_DATABASE = getenv("MYSQL_DATABASE")
MYSQL_HOSTNAME = getenv("MYSQL_HOSTNAME")
MYSQL_PORT = getenv("MYSQL_PORT")

DATABASE_CONNECTION_URI = f"mysql://{MYSQL_USERNAME}:{MYSQL_PASSWORD}@{MYSQL_HOSTNAME}:{MYSQL_PORT}/{MYSQL_DATABASE}"

class Config:
    SECRET_KEY = getenv("SECRET_KEY")


class DevelpmentConfig(Config):
    DEBUG = True
    HOST = "0.0.0.0"
    PORT = getenv("SERVER_LOCAL_PORT")


config = {"development": DevelpmentConfig}
