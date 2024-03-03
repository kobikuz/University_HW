import Animal
import Fish
import Crab
import Shrimp
import Scalar
import Moly
import Ocypode
STEPS_FOR_DEC_FOOD = 5

MAX_ANIMAL_HEIGHT = 8
MAX_ANIMAL_WIDTH = 8
MAX_CRAB_HEIGHT = 4
MAX_CRAB_WIDTH = 7
MAX_FISH_HEIGHT = 5
MAX_FISH_WIDTH = 8
WATERLINE = 3
FEED_AMOUNT = 10
MAX_AGE = 120
DIRECTION_LEFT = 0
DIRECTION_RIGHT = 1
DIRECTION_UP = 1
DIRECTION_DOWN = 0

class Aqua:
    def __init__(self, aqua_width, aqua_height):
        self.turn = 0
        self.aqua_height = aqua_height
        self.aqua_width = aqua_width
        self.board = [["  " for i in range(self.aqua_width)] for j in range(self.aqua_height)]
        self.build_tank()
        self.anim = []


    def build_tank(self):
        for row_index in range(self.aqua_height):
            if row_index != self.aqua_height-1:
                self.board[row_index][0] = "| "
                self.board[row_index][self.aqua_width-1] = " |"
                if row_index == WATERLINE-1:
                    for position in range(1,self.aqua_width-1):
                        self.board[row_index][position] = "~ "
            else:
                self.board[row_index][0] = "\\ "
                self.board[row_index][self.aqua_width-1] = " /"
                for position in range(1, self.aqua_width - 1):
                    self.board[row_index][position] = "_ "
        pass

    def clear_board(self):
        self.board = [["  " for i in range(self.aqua_width)] for j in range(self.aqua_height)]
        pass

    def print_board(self): #Runs in main
        self.clear_board()
        self.build_tank()
        for animal in self.anim:
            self.print_animal_on_board(animal)
        for row in self.board:
            print("".join(row))
        pass

    def get_board(self):
        return self.board
        pass

    def get_all_animal(self):
        """
        Returns the array that contains all the animals
        """
        return self.anim
        pass

    def is_collision(self, animal):
        """
        Returns True if the next step of the crab is a collision
        """
        for a in self.anim:
            if ((a.get_type() == "Crab") and (a != animal)
                    and (self.check_crab_collision(animal,a))):
                return True
        return False
        pass


    def print_animal_on_board(self, animal: Animal):
        image = animal.get_animal()
        w,h = animal.get_size()
        for x in range(0, w):
            for y in range(0, h):
                if image[y][x] != "  ":
                    self.get_board()[animal.get_y()+y][animal.get_x()+x] = image[y][x]
        pass


    def delete_animal_from_board(self, animal: Animal):
        self.anim.remove(animal)
        pass

    def add_fish(self, name, age, x, y, directionH, directionV, fishtype):
        """
        Adding fish to the aquarium
        """
        if fishtype == "sc":
            new_fish = Scalar.Scalar(name, age, x, y, directionH, directionV)
        elif fishtype == "mo":
            new_fish = Moly.Moly(name, age, x, y, directionH, directionV)
        else:
            return False
        self.anim.append(new_fish)
        return True
        pass

    def add_crab(self, name, age, x, y, directionH, crabtype):
        if crabtype == "oc":
            new_crab = Ocypode.Ocypode(name, age, x, y, directionH)
        elif crabtype == "sh":
            new_crab = Shrimp.Shrimp(name, age, x, y, directionH)
        else:
            return False
        self.anim.append(new_crab)
        return True
        pass

    def calculate_animals_range(self, animal):
        w,h = animal.get_size()
        x_min , x_max = animal.get_x(), (animal.get_x()+w)
        y_min , y_max = animal.get_y(), (animal.get_y()+h)
        return x_min ,x_max, y_min, y_max
        pass

    def check_crab_collision(self,one_animal, another_animal):
        x_min1, x_max1, y_min1 ,y_max1 = self.calculate_animals_range(one_animal)
        x_min2, x_max2, y_min2 ,y_max2 = self.calculate_animals_range(another_animal)
        if (x_min1 <= x_min2 <= x_max1):
            return True
        elif (x_min2 <= x_min1 <= x_max2):
            return True
        else:
            return False


    def check_place_occupied(self,animal_one, animals_two_x, animals_two_y): # animaltwo is the new animal
        x_min, x_max, y_min ,y_max = self.calculate_animals_range(animal_one)
        if ((x_min <= animals_two_x <= x_max)
            and
            (y_min <= animals_two_y <= y_max)):
            return True
        elif (( animals_two_x <= x_min <= animals_two_x +MAX_ANIMAL_WIDTH )
            and
            (animals_two_y <= y_min <= animals_two_y+MAX_ANIMAL_HEIGHT)):
            return True
        elif ((x_min <= animals_two_x <= x_max)
                and
              (y_min <= animals_two_y + MAX_ANIMAL_HEIGHT <= y_max)):
            return True
        elif ((animals_two_x <= x_min <= animals_two_x+MAX_ANIMAL_WIDTH)
              and
              (animals_two_y <= y_min <= animals_two_y+ MAX_ANIMAL_HEIGHT)):
            return True
        else:
            return False
        pass


    def check_if_free(self, animals_x, animals_y) -> bool:
        """
        method for checking whether the position is empty before inserting a new animal
        """
        for a in self.anim:
            if self.check_place_occupied(a, animals_x, animals_y):
                return False
        return True
        pass

    def current_crab_height(self): #not rellevant :( ( i thaught i need to calculate the height for the fishes)
        crab_height = 0
        for a in self.anim:
            if (a.get_type() == "Crab") and (a.get_height() > crab_height)  :
                crab_height = a.get_height()
        return crab_height

    def left(self, x=1):
        self.x = self.x + x
        pass

    def right(self, x=1):
        self.x = self.x-x
        pass

    def up(self, y=1):
        self.y = self.y -y
        pass

    def down(self, y=1):
        self.y = self.y +y
        pass

    def next_turn(self):
        """
        Managing a single step
        """
        self.turn += 1
        if ((self.turn % STEPS_FOR_DEC_FOOD  == 0) or (self.turn == 1)) :
            for a in self.anim:
                a.dec_food()
        if ((self.turn % 100 == 0) or (self.turn == 1)):
            for a in self.anim:
                a.inc_age()
                if a.age >= MAX_AGE:
                    a.die()
        for a in self.anim:
            if a.get_alive() == False:
                self.delete_animal_from_board(a)
        for subject in self.anim:
            if subject.get_type() == "Fish":
                self.moveV(subject)
            self.moveH(subject)
        collision_list = []
        for subject in self.anim:
            if ((subject.get_type() == "Crab")
                and
                (self.is_collision(subject) == True)):
                collision_list.append(subject)
        for subject in collision_list:
            if subject.get_directionH() == DIRECTION_LEFT:
                subject.set_directionH(DIRECTION_RIGHT)
            else:
                subject.set_directionH(DIRECTION_LEFT)
            self.moveH(subject)
            self.moveH(subject)
        pass

    def moveH(self, subject):
        w,h = subject.get_size()
        if subject.get_directionH() == DIRECTION_LEFT:
            if subject.get_x() > 1:
                subject.left()
            else:
                subject.set_directionH(DIRECTION_RIGHT)
        else:
            if subject.get_x() < (self.aqua_width - 2-w):
                subject.right()
            else:
                subject.set_directionH(DIRECTION_LEFT)

    def moveV(self, subject):
        w,h = subject.get_size()
        if subject.get_directionV() == DIRECTION_UP:
            if subject.get_y() > (WATERLINE):
                subject.up()
            else:
                subject.set_directionV(DIRECTION_DOWN)
        else:
            if subject.get_y() < (self.aqua_height - MAX_CRAB_HEIGHT -2 - h):
                subject.down()
            else:
                subject.set_directionV(DIRECTION_UP)

    def print_all(self):
        """
        Prints all the animals in the aquarium
        """
        for a in self.anim:
            print(a)
        pass

    def feed_all(self):
        """
        feed all the animals in the aquarium
        """
        for a in self.anim:
            a.food = a.food+FEED_AMOUNT
        pass

    def add_animal(self, name, age, x, y, directionH, directionV, animaltype):
        if self.check_if_free(x,y) == False : #todo: check inside each aninal type!
            return False

        if animaltype == 'sc' :
            delta_x = self.calculate_delta_x(x, Scalar.SCALAR_W)
            return self.add_fish(name, age, x-delta_x, y, directionH, directionV, animaltype)
        elif  animaltype == 'mo':
            delta_x = self.calculate_delta_x(x,Moly.MOLY_W)
            return self.add_fish(name, age, x-delta_x, y, directionH, directionV, animaltype)
        elif animaltype == 'oc' :
            delta_x = self.calculate_delta_x(x, Ocypode.OCYOPODE_W)
            return self.add_crab(name, age, x-delta_x, y, directionH, animaltype)
        elif  animaltype == 'sh':
            delta_x = self.calculate_delta_x(x, Shrimp.SHRIMP_W)
            return self.add_crab(name, age, x-delta_x, y, directionH, animaltype)
        else:
            return False

    def calculate_delta_x(self,x,animal_width):
        delta_x = x+animal_width -self.aqua_width+1
        if delta_x < 0:
            delta_x = 0
        return delta_x
        pass
    def several_steps(self, amount) -> None:
        """
        Managing several steps
        """
        for step in range(amount):
            self.next_turn()
        pass




