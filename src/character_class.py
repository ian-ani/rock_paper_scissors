# PYTHON VERSION: 3.11.9

class Character():

    def __init__(self, counter, life):
        self.counter = counter
        self.life = life

    def set_counter(self, counter):
        self.counter = counter

    def set_life(self, life):
        self.life = life

    def get_counter(self):
        return self.counter

    def get_life(self):
        return self.life
    