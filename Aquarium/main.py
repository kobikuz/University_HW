import time #TODO: IMPORT TIME
import Aqua
DIRECTION_LEFT = 0
DIRECTION_RIGHT = 1
DIRECTION_UP = 1
DIRECTION_DOWN = 0
SHRIMP_HEIGHT = 3
OCYOPODE_HEIGHT = 4
WATERLINE = 3
MAX_ANIMAL_HEIGHT = 8
MAX_ANIMAL_WIDTH = 8

def demo(myaqua): #TODO:DEmo
    """
    Running a demo aquarium
    for example:
    myaqua.add_animal("scalarfish1", 4, 10, 10, 1, 0, 'sc')
    myaqua.add_animal("molyfish2", 12, 35, 15, 0, 1, 'mo')
    myaqua.add_animal("shrimpcrab1", 3, 20, myaqua.aqua_height, 1, 0, 'sh')
    myaqua.add_animal("ocypodecrab2", 13, 41, myaqua.aqua_height, 0, 0, 'oc')
    myaqua.print_board()

    for i in range(120):
        ....
    """
    myaqua.add_animal("scalarfish1", 4, 1, WATERLINE+1, 1, 0, 'sc')
    myaqua.add_animal("molyfish2", 4, 15, WATERLINE+1, 0, 1, 'mo')
    myaqua.add_animal("shrimpcrab1", 3, 10, myaqua.aqua_height - SHRIMP_HEIGHT - 1, 1, 0, 'sh')
    myaqua.add_animal("ocypodecrab2", 13, 25, myaqua.aqua_height - OCYOPODE_HEIGHT - 1, 0, 0, 'oc')
    for i in range(120):
        for a in myaqua.anim:
            if a.get_food() < 3:
                myaqua.feed_all()
                break
        myaqua.next_turn()
        myaqua.print_board()
        time.sleep(0.5)


def check_in_range(inp,options,min = 0):
    try :
          result = int(inp)
    except:
        return -1
    if result in range(min,options+1):
        return result
    else:
        return -1

def check_if_bigger(age,min_value):
    try:
       result =  int(age)
    except:
        return -1
    if result >= min_value:
        return result
    else:
        return -1

def several_steps(myaqua):
    move_on = True
    while move_on:
        steps = input("How many steps do you want to take?")
        steps = check_in_range(steps,100000000)
        move_on = steps < 0
    myaqua.several_steps(steps)
    return None

def add_animal(myaqua):
    choice = 0
    move_on = True
    while move_on:
        print("Please select:")
        print("1. Scalare")
        print("2. Moly")
        print("3. Ocypode")
        print("4. Shrimp")
        choice = input("What animal do you want to put in the aquarium?")
        choice = check_in_range(choice,4)
        move_on = choice <= 0

    name = input("Please enter a name:")
    age = 0
    move_on =True
    while  move_on == True:
        age = input("Please enter age:")
        age = check_in_range(age,100)
        move_on = age < 0

    success = False
    while not success:
        x, y = 0, 0
        move_on = True
        while move_on:
            while move_on == True:
                x = input("Please enter an X axis location (1 - %d):" % (myaqua.aqua_width - 1))
                x=check_in_range(x,myaqua.aqua_width-1)
                move_on = x < 0
            move_on = True
            if choice == 1 or choice == 2:
                while move_on == True:
                    y = input("Please enter an Y axis location (%d - %d):" % (WATERLINE+1, myaqua.aqua_height -1))
                    min_height = myaqua.current_crab_height()
                    y = check_in_range(y,myaqua.aqua_height - min_height-1-MAX_ANIMAL_HEIGHT,WATERLINE)
                    if y < 0:
                        print("This place is not available! Please try again later.")
                        move_on = True
                    else:
                        move_on = False
            if myaqua.check_if_free(x,y) == False:
                print("This place is not available! Please try again later.")
                move_on = True
            else:
                move_on = False
        directionH, directionV = -1, -1
        move_on = True
        while move_on == True:
            directionH = input("Please enter horizontal direction (0 for Left, 1 for Right):")
            directionH = check_in_range(directionH,1)
            move_on = directionH < 0

        move_on = True
        if choice == 1 or choice == 2:
            while move_on == True:
                directionV = input("Please enter vertical direction  (0 for Down, 1 for Up):")
                directionV = check_in_range(directionV,1)
                move_on = directionV < 0

        if choice == 1:
            success = myaqua.add_animal(name, age, x, y, directionH, directionV, 'sc')
        elif choice == 2:
            success = myaqua.add_animal(name, age, x, y, directionH, directionV, 'mo')
        elif choice == 3:
            success = myaqua.add_animal(name, age, x, myaqua.aqua_height - OCYOPODE_HEIGHT - 1, directionH, None, 'oc')
        else:
            success = myaqua.add_animal(name, age, x, myaqua.aqua_height - SHRIMP_HEIGHT - 1, directionH, None, 'sh')

    return None


if __name__ == '__main__':
    width = 0
    height = 0
    move_on = True

    print('Welcome to "The OOP Aquarium"')
    while move_on:
        width = input("The width of the aquarium (Minimum 40): ")
        width = check_if_bigger(width,40)
        move_on = width < 0
    move_on = True
    while move_on:
        height = input("The height of the aquarium (Minimum 25): ")
        height = check_if_bigger(height,25)
        move_on = height < 0

    myaqua = Aqua.Aqua(width, height)
    myaqua.print_board()

    while True:
        choice = 0
        move_on = True
        while move_on:
            print("Main menu")
            print("-" * 30)
            print("1. Add an animal")
            print("2. Drop food into the aquarium")
            print("3. Take a step forward")
            print("4. Take several steps")
            print("5. Demo")
            print("6. Print all")
            print("7. Exit")

            choice = input("What do you want to do?")
            choice = check_in_range(choice,7)
            move_on = choice <= 0

        if choice == 1:
            add_animal(myaqua)
        elif choice == 2:
            myaqua.feed_all()
        elif choice == 3:
            myaqua.next_turn()
        elif choice == 4:
            several_steps(myaqua)
        elif choice == 5:
            demo(myaqua)
        elif choice == 6:
            myaqua.print_all()
        elif choice == 7:
            print("Bye bye")
            exit()

        myaqua.print_board()
