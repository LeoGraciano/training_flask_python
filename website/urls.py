
def url_routers(app):
    from website.apps.core.views import core_views
    from website.apps.account.auth import account_views

    app.register_blueprint(core_views, url_prefix="/")
    app.register_blueprint(account_views, url_prefix="/")

    return app
