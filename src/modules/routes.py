from .users.blueprint import blueprint as users_blueprint


def register_routes(app):
    app.register_blueprint(users_blueprint, url_prefix="/users")
