import Crab
SHRIMP_W = 7
SHRIMP_H = 3
DIRECTION_LEFT = 0
DIRECTION_RIGHT = 1
DIRECTION_UP = 1
DIRECTION_DOWN = 0

class Shrimp(Crab.Crab):
    def __init__(self, name, age, x, y, directionH):
        super().__init__(name, age, x, y, directionH)
        self.width = SHRIMP_W
        self.height = SHRIMP_H
        self.image_left =  [["* ","  ","* ","  ","  ","  ","  "],
                            ["  ","* ","* ","* ","* ","* ","* "],
                            ["  ","  ","* ","  ","* ","  ","  "]]
        self.image_right = [["  ","  ","  ","  ","* ","  ","* "],
                            ["* ","* ","* ","* ","* ","* ","  "],
                            ["  ","  ","* ","  ","* ","  ","  "]]
        pass

    def get_animal(self):
        if self.directionH == DIRECTION_LEFT:
            return self.image_left
        else:
            return self.image_right
        pass

    def get_height(self):
        return self.height
