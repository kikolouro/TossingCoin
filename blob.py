import random


class Blob:
    def __init__(self, ischeater):
        self.ischeater = ischeater
        self.points = 0

    def tossCoing(self):
        value = random.random()

        if self.ischeater:
            if value + 0.3 > 1:
                value = 1
            else:
                value += 0.3

        if value > 0.5:
            return "Heads"
        else:
            return "Tails"
    
    def addPoints(self, points):
        self.points += points
        return self.points

    def ifcheater(self):
        return self.ischeater