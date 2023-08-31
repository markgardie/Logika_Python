

class Result():

    def __init__(self):
        self.rest_pulse = None
        self.activity_pulse = None
        self.end_pulse = None

        self.index = None
        self.level = None
        self.result = None

    def ruffier_index(self):

        self.index = ( 4 * (self.rest_pulse + self.activity_pulse + self.end_pulse) - 200 ) / 10

    
    def bad_level(self, age):

        norm_age = (min(age, 15) - 7) / 2
        self.level = 21 - norm_age * 1.5


    def final_result(self):

        if self.index >= self.level:
            self.result = 0

        level = level - 4 
        if self.index >= self.level:
            self.result = 1

        level = level - 5 
        if self.index >= self.level:
            self.result = 2

        level = level - 5.5 
        if self.index >= self.level:
            self.result = 3
            
        self.result = 4
        
    

        