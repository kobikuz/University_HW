import Crab
OCYOPODE_W = 7
OCYOPODE_H = 4
DIRECTION_LEFT = 0
DIRECTION_RIGHT = 1
DIRECTION_UP = 1
DIRECTION_DOWN = 0

class Ocypode(Crab.Crab):
    def __init__(self, name, age, x, y, directionH):
        super().__init__(name, age, x, y, directionH)
        self.width = OCYOPODE_W
        self.height = OCYOPODE_H
        self.image =[["  ", "* ", "  ", "  ", "  ", "* ", "  "],
                     ["  ", "  ", "* ", "* ", "* ", "  ", "  "],
                     ["* ", "* ", "* ", "* ", "* ", "* ", "* "],
                     ["* ", "  ", "  ", "  ", "  ", "  ", "* "]]
        pass

    def get_animal(self):
        return self.image
        pass

    def get_height(self):
        return self.height