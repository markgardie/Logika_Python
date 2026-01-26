

class Car:

    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def ride(self):
        print(f"Car {self.name} is riding with speed {self.speed}")

    @staticmethod
    def hello():
        print("Hello")


Car.hello()
