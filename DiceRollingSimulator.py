import random

x = input("press y to roll again and n to exit:")

while x == "y":
    no = random.randint(1, 6)
    if no == 1:
        print(" _____ ")
        print("|     |")
        print("|  0  |")
        print("|     |")
        print("|_____|")
    if no == 2:
        print(" _____ ")
        print("| 0   |")
        print("|     |")
        print("|   0 |")
        print("|_____|")
    if no == 3:
        print(" _____ ")
        print("| 0   |")
        print("|  0  |")
        print("|   0 |")
        print("|_____|")
    if no == 4:
        print(" _____")
        print("| 0 0 |")
        print("|     |")
        print("| 0 0 |")
        print("|_____|")
    if no == 5:
        print(" _____ ")
        print("| 0 0 |")
        print("|  0  |")
        print("| 0 0 |")
        print("|_____|")
    if no == 6:
        print(" _____ ")
        print("| 0 0 |")
        print("| 0 0 |")
        print("| 0 0 |")
        print("|_____|")
    print("\n")
    x=input("press y to roll again and n to exit:")