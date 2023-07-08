from app import app
from utils.db import db
from config import config

db.init_app(app)
with app.app_context():
    try:
        db.create_all()
    except Exception as e:
        print('ERROR VERIFYING DATABASE CONNECTION: ', str(e))

if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.run(port=app.config['PORT'], host=app.config['HOST'])