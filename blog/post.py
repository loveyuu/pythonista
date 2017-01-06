# encoding=utf-8
from flask import Blueprint
from flask.views import MethodView

post = Blueprint('post', __name__)


class Post(MethodView):
    def get(self, post_id):
        if post_id is None:
            return 'this is post list'
        else:
            return "this is get post {}".format(post_id)

    def post(self):
        pass

    def delete(self):
        pass

    def put(self):
        pass

post_view = Post.as_view('post')
post.add_url_rule(
    '/posts/',
    defaults={'post_id': None},
    view_func=post_view,
    methods=['GET'],
)

post.add_url_rule(
    '/posts/',
    view_func=post_view,
    methods=['POST'],
)

post.add_url_rule(
    '/posts/<int:post_id>',
    view_func=post_view,
    methods=['GET', 'PUT', 'DELETE'],
)
