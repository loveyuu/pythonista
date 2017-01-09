# encoding=utf-8
from flask import Flask
from config import config


def blog_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    from .post import post as post_blueprint
    app.register_blueprint(post_blueprint)

    from .comment import comment as comment_blueprint
    app.register_blueprint(comment_blueprint)

    from .user import user as user_blueprint
    app.register_blueprint(user_blueprint)

    @app.errorhandler(404)
    def page_not_found(e):
        return 'no such resource', 404

    @app.errorhandler(500)
    def internal_server_error(e):
        return 'server gone', 500

    return app
