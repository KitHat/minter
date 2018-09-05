from minter.views import mint, transfer


def setup_routes(app):
    app.router.add_post('/mint', mint)
    app.router.add_post('/transfer', transfer)