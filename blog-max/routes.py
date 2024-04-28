from controllers.main_controller import MainController


class BlogRoutes():

    def __init__(self):
        self.main_controller = MainController()

    def setup_routes(self, app):
        app.add_url_rule('/', 'index', self.main_controller.index)
        app.add_url_rule('/<int:post_id>', 'post', self.main_controller.post)
        app.add_url_rule('/create', 'create', self.main_controller.create, methods=['GET', 'POST'])
        app.add_url_rule('/edit/<int:post_id>', 'edit', self.main_controller.edit, methods=['GET', 'POST'])
        app.add_url_rule('/delete/<int:post_id>', 'delete', self.main_controller.delete, methods=['GET', 'POST'])
        app.add_url_rule('/about', 'about', self.main_controller.about)