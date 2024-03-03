import Animal

MAX_FISH_HEIGHT = 5
MAX_FISH_WIDTH = 8


class Fish(Animal.Animal):
    def __init__(self, name, age, x, y, directionH, directionV):
        super().__init__(name, age, x, y, directionH)
        self.width = MAX_FISH_WIDTH
        self.height = MAX_FISH_HEIGHT
        self.directionV = directionV  # random 0 - down / 1 - up


    def __str__(self):
        st = "The fish " + super().__str__()
        return st

    def up(self):
        self.y = self.y-1
        pass

    def down(self):
        self.y = self.y+1
        pass

    def starvation(self):
        print("The fish %s died at the age of %d years\nBecause he ran out of food!" % (self.name, self.age))
        super(Fish, self).starvation()
        pass

    def die(self):
        super(Fish, self).die()
        pass

    def get_directionV(self):
        return self.directionV
        pass

    def set_directionV(self, directionV):
        self.directionV = directionV
        pass

    def get_type(self):
        return "Fish"