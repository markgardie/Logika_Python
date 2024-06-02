from controllers.main_controller import MainController

class BlogRoutes():

    def __init__(self):
        self.controller = MainController()

    def setup_routes(self, app):
        app.add_url_rule("/", "index", self.controller.index)
        app.add_url_rule("/create", "create", self.controller.create, methods = ["GET", "POST"])
        app.add_url_rule("/edit/<int:id>", "edit", self.controller.edit, methods = ["GET", "POST"])
        
        