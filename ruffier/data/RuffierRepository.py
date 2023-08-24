

class RuffierRepository():
    
    def __init__(self) :
        self.results = []
        self.name = None
        self.age = None

    def set_user(self, name, age):
        self.name = name
        self.age = age

    def add_result(self, result):
        self.results.append(result)

    def clear(self):
        self.results.clear()