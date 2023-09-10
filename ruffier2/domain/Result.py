

class Result():

    def __init__(self):
        self.rest_pulse = None
        self.activity_pulse = None
        self.end_pulse = None

        self.ruffier_index = None
        self.level = None
        self.final_result = None

    def calculate_ruffier(self):

        self.ruffier_index = ( 4 * (self.rest_pulse + self.activity_pulse + self.end_pulse) - 200 ) / 10


    def bad_level(self, age):

        norm_age = (min(age, 15) - 7) / 2
        self.level = 21 - norm_age * 1.5

    def calculate_result(self):

        if self.ruffier_index > self.level:
            self.final_result = 0 

        self.level -= 4

        if self.ruffier_index > self.level:
            self.final_result = 1

        self.level -= 5

        if self.ruffier_index > self.level:
            self.final_result = 2

        self.level -= 5.5

        if self.ruffier_index > self.level:
            self.final_result = 3

        self.level -= 5

        if self.ruffier_index < self.level:
            self.final_result = 4

         