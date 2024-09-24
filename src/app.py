from http import HTTPStatus

from alchemical.flask import Alchemical
from apifairy import APIFairy, response
from flask import Flask, jsonify, redirect, url_for
from flask_cors import CORS
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from config import Config

apifairy = APIFairy()
db = Alchemical()
cors = CORS()
ma = Marshmallow()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    migrate = Migrate(app=app, db=db)
    db.init_app(app)
    ma.init_app(app)
    if app.config['FLASK_CORS']:
        cors.init_app(app)
    apifairy.init_app(app)

    from .routes.item_route import items
    app.register_blueprint(items)
    from .routes.user_route import users
    app.register_blueprint(users)
    from .routes.author_route import authors
    app.register_blueprint(authors)
    from .routes.publisher_route import publishers
    app.register_blueprint(publishers)

    @app.route('/')
    def index():
        return redirect(url_for('apifairy.docs'))

    @response({'status': 'ok'}, HTTPStatus.OK)
    @app.route('/healthcheck')
    def healthcheck():
        """Verificação de status da api

        Returns:
            body: status
        """
        return jsonify({'status': 'ok'})

    return app
