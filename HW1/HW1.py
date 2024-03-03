def Question1():
    str = input()
    vowels = ["a", "e", "i", "u", "o", "y"]
    num = 0
    alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    for i in range(len(str)):
        if str[i] not in vowels and str[i] in alphabet_list:
            num = num+1
    print(num)
    exit()


def Question2():
    def no_spaces(str):
        for i in range(len(str)):
            if str[i] == " ":
                exit()

    try:
        x = input()
        n = input()
        no_spaces(x)
        no_spaces(n)
        x = float(x)
        n = float(n)
    except:
        print("error")
        exit()

    if n % 1 != 0:
        print("error")
        exit()


    if x < -0.7 or x > 0.7:
        print("error")
        exit()


    if n < 0 :
        print("error")
        exit()


    def taylor_series(num, power):
        sum = 0
        for i in range(1, power + 1):
            partial_sum = (num ** i) * (((-1) ** (i - 1)) / i)
            sum = sum + partial_sum
        return sum

    taylor_sum = taylor_series(x, int(n))
    print(taylor_sum)
    exit()


def Question3():
    str = list(input().split())
    Evenwords = []
    Oddwords = []
    for i in range(len(str)):
        if i % 2 == 0:
            Oddwords.append(str[i].upper())
        else:
            Evenwords.append(str[i].lower())
    Oddwords.sort()
    Evenwords.sort(reverse=True)

    print(" ".join(Oddwords) + " " + " ".join(Evenwords))
    exit()


def Question4():
    def Step(num):
        Reversenum = num[::-1]
        num = int(num) + int(Reversenum)
        num = str(num)
        return num

    def IsPoli(num):
        if len(num) < 1:
            print("error")
            exit()
        if len(num) == 1:
            print("0")
            exit()
        numReversed = num[::-1]
        for k in range(len(num) // 2):
            if numReversed[k] != num[k]:  # the num is POLI!
                return False
        return True

    InputNum = input()
    for i in range(501):
        if IsPoli(InputNum):
            print(i)
            exit()
        InputNum = Step(InputNum)
    print("True")
    exit()


Question_number = input()
if Question_number == "1":
    Question1()
elif Question_number == "2":
    Question2()
elif Question_number == "3":
    Question3()
elif Question_number == "4":
    Question4()
else:
    print("error")
exit()