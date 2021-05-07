def oops():
    raise IndexError
    # raise KeyError


def another_function():
    try:
        oops()
    except IndexError:
        print("My index Error")


def get_some_data(a, b):
    try:
        return int(a) ** 2 / int(b)
    except ValueError:
        print("Value ERROR")
    except ZeroDivisionError:
        print("ZeroDivision")


if __name__ == '__main__':
    # Task 1
    """
    Write a function called oops that explicitly raises an IndexError exception when called. 
    Then write another function that calls oops inside a try/except statement  to catch the error. 
    What happens if you change oops to raise KeyError instead of IndexError?
    """
    another_function()
    print("FINISH")

    # Task 2
    """
    Write a function that takes in two numbers from the user via input(), call the numbers a and b, 
    and then returns the value of squared a divided by b, construct a try-except block which raises an exception 
    if the two values given by the input function were not numbers, and if value b was zero (cannot divide by zero).  
    """
    c = get_some_data(input("Write a first number- "), input("Write a second number- "))
    print(c)
