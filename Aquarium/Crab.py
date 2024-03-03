import Animal
MAX_CRAB_HEIGHT = 4
MAX_CRAB_WIDTH = 7


class Crab(Animal.Animal):
    def __init__(self, name, age, x, y, directionH):
        super().__init__(name, age, x, y, directionH)
        pass

    def __str__(self):
        st = "The Crab " + super().__str__()
        return st
        pass

    def starvation(self):
        print("The Crab %s died at the age of %d years\nBecause he ran out of food!" % (self.name, self.age))
        super(Crab, self).starvation()
        pass

    def die(self):
        super(Crab, self).die()
        pass

    def get_type(self):
        return "Crab"