import Fish
SCALAR_W =8
SCALAR_H =5
DIRECTION_LEFT = 0
DIRECTION_RIGHT = 1
DIRECTION_UP = 1
DIRECTION_DOWN = 0


class Scalar(Fish.Fish):
    def __init__(self, name, age, x, y, directionH, directionV):
        super().__init__(name, age, x, y, directionH, directionV)
        self.width = SCALAR_W
        self.height = SCALAR_H
        self.image_left =  [["  ", "  ", "* ", "* ", "* ", "* ", "* ","* "],
                            ["  ", "* ", "* ", "* ", "  ", "  ", "  ","  "],
                            ["* ", "* ", "* ", "* ", "* ", "* ", "  ","  "],
                            ["  ", "* ", "* ", "* ", "  ", "  ", "  ","  "],
                            ["  ", "  ", "* ", "* ", "* ", "* ", "* ","* "]]

        self.image_right = [["* ", "* ", "* ", "* ", "* ", "* ", "  ", "  "],
                            ["  ", "  ", "  ", "  ", "* ", "* ", "* ", "  "],
                            ["  ", "  ", "* ", "* ", "* ", "* ", "* ", "* "],
                            ["  ", "  ", "  ", "  ", "* ", "* ", "* ", "  "],
                            ["* ", "* ", "* ", "* ", "* ", "* ", "  ","  "]]

    def get_animal(self):
        if self.directionH == DIRECTION_LEFT:
            return self.image_left
        else:
            return self.image_right
        pass


    def get_height(self):
        return self.height
