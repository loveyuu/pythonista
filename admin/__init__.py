# encoding=utf-8
from flask import Flask
from config import config
from flask_bootstrap import Bootstrap
from flask_redis import FlaskRedis


bootstrap = Bootstrap()
redis_store = FlaskRedis()


def admin_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    redis_store.init_app(app)

    from .user import user as user_blueprint
    app.register_blueprint(user_blueprint)

    @app.errorhandler(404)
    def page_not_found(e):
        return 'no such resource', 404

    @app.errorhandler(500)
    def internal_server_error(e):
        return 'server gone', 500

    return app
