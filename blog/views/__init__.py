# encoding=utf-8
from .comment import comment as comment_blueprint
from .post import post as post_blueprint
from .user import user as user_blueprint

blueprints = (
    post_blueprint,
    comment_blueprint,
    user_blueprint
)
