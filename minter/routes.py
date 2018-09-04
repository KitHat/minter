from minter.views import transfer


def setup_routes(app):
    app.router.add_post('/transfer', transfer)