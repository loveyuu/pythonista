# encoding=utf-8
from flask import Blueprint, render_template

from admin import redis_store

user = Blueprint('user', __name__)


@user.route('/index/')
def index():
    return render_template('index.html')


@user.route('/settings/')
def settings():
    members = redis_store.provider_class.lrange('member', 0, -1)
    print members
    return "yes it is"
