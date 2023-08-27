

class Result():

    def __init__(self):
        self.rest_pulse = None
        self.activity_pulse = None
        self.end_pulse = None

        self.ruffier_index = None

    def calculate_ruffier(self):

        self.ruffier_index = ( 4 * (self.rest_pulse + self.activity_pulse + self.end_pulse) - 200 ) / 10

        