# encoding=utf-8
def register_error(app):
    @app.errorhandler(404)
    def page_not_found(e):
        return 'no such resource', 404

    @app.errorhandler(500)
    def internal_server_error(e):
        return 'server gone', 500
