from flask import Flask

from website.urls import url_routers


def create_app():
    app = Flask(__name__)
    # app.config.from_object('config')
    app.config['SECRET_KEY'] = '123456789123456789'

    app = url_routers(app)

    return app
