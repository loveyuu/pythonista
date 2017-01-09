# encoding=utf-8
from flask import Blueprint
from flask.views import MethodView

comment = Blueprint('comment', __name__)


class Comment(MethodView):
    def get(self, user_id, post_id):
        return "this is get {} {}comment".format(user_id, post_id)

    def delete(self):
        pass

    def put(self):
        pass

comment_view = Comment.as_view('comment')
comment.add_url_rule(
    '/users/<int:user_id>/posts/<int:post_id>/comments/',
    view_func=comment_view,
    methods=['GET']
)

comment.add_url_rule(
    '/users/<int:user_id>/posts/<int:post_id>/comments/',
    view_func=comment_view,
    methods=['POST'],
)

comment.add_url_rule(
    '/users/<int:user_id>/posts/<int:post_id>/comments/<int:comment_id>/',
    view_func=comment_view,
    methods=['GET', 'PUT', 'DELETE'],
)