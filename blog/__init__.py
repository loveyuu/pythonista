# encoding=utf-8
from flask import Flask
from config import config


def blog_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    # 注册蓝图组件
    from .views import blueprints
    for b in blueprints:
        app.register_blueprint(b)

    # 注册错误处理
    from .errors import register_error
    register_error(app)

    return app
