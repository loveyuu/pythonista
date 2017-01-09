# encoding=utf-8
from flask import Blueprint, request, jsonify

sign = Blueprint('sign', __name__)


@sign.route('/signin/')
def signin():
    data = request.get_json()
    return jsonify(data)


@sign.route('/signup/')
def signup():
    data = request.get_json()
    return jsonify(data)


@sign.route('/signout/')
def signout():
    data = request.get_json()
    return jsonify(data)
