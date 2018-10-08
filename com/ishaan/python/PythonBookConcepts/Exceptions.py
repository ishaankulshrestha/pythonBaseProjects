flag = True
while flag:
    try:
        a,b = (int(x) for x in input("Enter any 2 numbers \n\n").split(" "))
        c = a/b
        print("Answer of {}/{} is {}".format(a,b,c))
        flag = False
    except EnvironmentError:
        print("Provide correct values of inputs !")
    except ZeroDivisionError:
        print("Division by zero, Try again!")
    except:
        print("Some other error. Try again ")
    finally:
        print("I am inside finally")
