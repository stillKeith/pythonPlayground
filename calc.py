import os

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def per(x, y):
    return x * y / 100

def div(x, y):
    return x / y
repeat = True
while repeat:

    print("select option")
    print("add:1 ")
    print("sub:2 ")
    print("mul:3 ")
    print("div:4 ")
    print("per:5 ")

    choice = int(input("What do you want to do:"))



    if choice == 1:
        num1 = int(input("first num "))
        num2 = int(input("second num "))
        print(add(num1, num2))

    elif choice == 2:
        num1 = int(input("first num "))
        num2 = int(input("second num "))

        print(sub(num1, num2))

    elif choice == 3:
        num1 = int(input("first num "))
        num2 = int(input("second num "))
        print(mul(num1, num2))

    elif choice == 4:
        num1 = int(input("first num "))
        num2 = int(input("second num "))
        print(div(num1, num2))
    elif choice == 5:
        num1 = int(input("first num "))
        num2 = int(input("second num "))
        print(div(num1, num2))


    else:
        print("invaild")

    val = input("repeat?")
    if val == "yes":
        repeat = True
    else:
        repeat = False

print ("See Ya now!")

