# encoding=utf-8
from flask import Blueprint
from flask.views import MethodView

comment = Blueprint('comment', __name__)


class Comment(MethodView):
    def get(self):
        return "this is get comment"

    def delete(self):
        pass

    def put(self):
        pass

comment.add_url_rule('/', view_func=Comment.as_view('comment'), methods=['GET'])
