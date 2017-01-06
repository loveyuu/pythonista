# encoding=utf-8
from flask import Blueprint
from flask.views import MethodView

user = Blueprint('user', __name__)


class User(MethodView):
    def get(self):
        return "this is get user"

    def delete(self):
        pass

    def put(self):
        pass

user_view = User.as_view('user')
user.add_url_rule('/users', view_func=user_view, methods=['GET'])
