from werkzeug.wsgi import DispatcherMiddleware
from flask import Flask
from admin import admin_app
from blog import blog_app

app = Flask(__name__)
admin_app = admin_app('dev')

blog_app = blog_app('dev')

app.wsgi_app = DispatcherMiddleware(
    app.wsgi_app,
    {
        '/admin': admin_app,
        '/blog': blog_app
    }
)
