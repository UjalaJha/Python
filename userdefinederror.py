class Error(Exception):
    """Base class for exception"""
class ValueSmallError(Exception):
    """Raised for very small value"""
    pass
class ValueLargeError(Exception):
    """Raised for very large value"""
    pass

number=10
while True:
    try:
        num=int(input("Enter Number : "))
        if num<number:
                raise ValueSmallError
        elif num>number:
                raise ValueLargeError

    except ValueSmallError:
        print("This value is too small, try again!")
        print()
    except ValueLargeError:
        print("This value is too large, try again!")
        print()
    else:
        print("Congratulations! You guessed it correctly.")
