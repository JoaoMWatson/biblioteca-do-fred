from http import HTTPStatus

from alchemical.flask import Alchemical
from apifairy import APIFairy, response
from flask import Flask, jsonify, redirect, url_for
from flask_cors import CORS
from flask_marshmallow import Marshmallow

from config import Config

apifairy = APIFairy()
db = Alchemical()
cors = CORS()
ma = Marshmallow()


def create_app():
    # Main
    app = Flask(__name__)
    app.config.from_object(Config)

    ma.init_app(app)
    if app.config['FLASK_CORS']:
        cors.init_app(app)
    apifairy.init_app(app)
    db.init_app(app)

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