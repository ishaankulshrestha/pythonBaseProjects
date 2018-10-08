flag = True

while flag:
    num = int(input("Enter a number smaller than 10 \n\n"))
    try:
        assert num < 10
        print("You have entered correct option")
        flag = False
    except:
        print("Value entered by you is not correct. Try again.")
    finally:
        print("I am inside finally")