from controllers.main_controller import MainController

main_controller = MainController()

def setup_routes(app):
    app.add_url_rule("/", "index", main_controller.index)