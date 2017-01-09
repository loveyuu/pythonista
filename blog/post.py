# encoding=utf-8
from flask import Blueprint
from flask.views import MethodView

post = Blueprint('post', __name__)


class Post(MethodView):
    def get(self, user_id, post_id):
        if post_id is None:
            return 'this is {} post list'.format(user_id)
        else:
            return "this is {} get post {}".format(user_id, post_id)

    def post(self, user_id):
        pass

    def delete(self):
        pass

    def put(self):
        pass

post_view = Post.as_view('post')
post.add_url_rule(
    '/users/<int:user_id>/posts/',
    defaults={'post_id': None},
    view_func=post_view,
    methods=['GET'],
)

post.add_url_rule(
    '/users/<int:user_id>/posts/',
    view_func=post_view,
    methods=['POST'],
)

post.add_url_rule(
    '/users/<int:user_id>/posts/<int:post_id>/',
    view_func=post_view,
    methods=['GET', 'PUT', 'DELETE'],
)
