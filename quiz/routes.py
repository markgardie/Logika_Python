from controllers.main_controller import MainController

main_controller = MainController()

def setup_routes(app):
    app.add_url_rule("/", "index", main_controller.index, methods = ["post", "get"])
    app.add_url_rule("/quiz", "quiz", main_controller.quiz, methods = ["post", "get"])
    app.add_url_rule("/result", "result", main_controller.result, methods = ["get"])
    