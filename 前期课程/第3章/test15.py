# coding:utf-8

while True:
    try:
        age = int(input("How old are you?"))
        if age > 150:
            raise ValueError("Are you a god?")
        elif (age <= 150) and (age > 80):
            print("Wish you good health.")
        elif (age <= 80) and (age > 60):
            print("A new life begins")
        elif (age <= 60) and (age > 30):
            print("Work hard")
        else:
            print("I envy you.")
    except (ValueError, AssertionError):
        print("find your glasses.")
        break
