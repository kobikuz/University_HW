MAX_ANIMAL_HEIGHT = 8
MAX_ANIMAL_WIDTH = 8
STARTING_FOOD = 5 # needs to be 5
MAX_AGE = 120 # needs to be 120
DIRECTION_LEFT = 0
DIRECTION_RIGHT = 1
DIRECTION_UP = 1
DIRECTION_DOWN = 0

class Animal:
    def __init__(self, name, age, x, y, directionH):
        self.alive = True
        self.width = MAX_ANIMAL_WIDTH
        self.height = MAX_ANIMAL_HEIGHT
        self.food = STARTING_FOOD
        self.name = name
        self.age = age
        self.x = x
        self.y = y
        self.directionH = directionH  # random 0 - left / 1 - right

    def __str__(self):
        return  str(self.name) + " is " + str(self.age) + " years old and has " + str(self.food) + " food"
        pass

    def get_food(self):
        return self.food
        pass

    def get_age(self):
        return self.age
        pass

    def dec_food(self):
        self.food = self.food - 1
        if self.food == 0:
            self.starvation()
        pass

    def inc_age(self):
        self.age += 1
        pass

    def right(self):
        self.x = self.x+1
        pass

    def left(self):
        self.x = self.x-1
        pass

    def get_position(self):
        return (self.x, self.y)
        pass

    def set_x(self, x):
        self.x = x
        pass

    def get_x(self):
        return self.x
        pass

    def set_y(self, y):
        self.y = y
        pass

    def get_y(self):
        return self.y

    def starvation(self):
        self.alive = False
        pass

    def die(self):
        """
        the animal died because its very old
        :return:
        """
        print("%s died in good health" % (self.name))
        self.alive = False
        pass

    def get_directionH(self):
        return self.directionH
        pass

    def set_directionH(self, directionH):
        self.directionH = directionH
        pass

    def get_alive(self):
        return self.alive
        pass

    def get_size(self):
        return (self.width,self.height)
        pass

    def get_food_amount(self):
        return self.food
        pass

    def add_food(self, amount):
        self.food = self.food +amount
        pass

    def get_animal(self):
        # LEAVE IT BE!
        pass

    def get_type(self):
        return None

    def get_height(self):
        return self.height