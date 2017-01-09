# encoding=utf-8
from flask import Blueprint, request, jsonify
from flask.views import MethodView

user = Blueprint('user', __name__, url_prefix='/users')


class User(MethodView):
    def get(self):
        return "get"

    def post(self):
        data = request.get_json()
        return jsonify(data)


class Signin(MethodView):
    def post(self):
        data = request.get_json()
        return jsonify(data)

user_view = User.as_view('user')
signin_view = Signin.as_view('signin')

user.add_url_rule(
    '/',
    view_func=user_view,
    methods=['GET'],
)

user.add_url_rule(
    '/',
    view_func=user_view,
    methods=['POST'],
)

user.add_url_rule(
    '/signins/',
    view_func=signin_view,
    methods=['POST'],
)
