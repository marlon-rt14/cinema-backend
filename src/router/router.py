from flask import Blueprint

from .routes import movies

router = Blueprint('router', __name__)

router.register_blueprint(movies, url_prefix='/movies')

