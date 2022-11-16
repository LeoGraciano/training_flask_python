
def url_routers(app):
    from website.apps.account.views import views
    from website.apps.account.auth import auth

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    return app
