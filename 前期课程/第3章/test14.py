# coding:utf-8

while True:
    try:
        x = int(input("input an int:"))
        r = 10 / x
        print(r)
    except (ZeroDivisionError, SyntaxError) as e:
        print(e)
        # print("you should not input zero.")
        break
    finally:
        print("goodbye.")
        break
    # except SyntaxError:
        # print("input a number.")
