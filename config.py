# encoding=utf-8
class Config(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):

    SQLALCHEMY_DATABASE_URI = 'mysql://root:111111@localhost/orange'
    DEBUG = False


config = {
    'dev': DevelopmentConfig,
}
