import random
def greet(name):
    """prints a greeting for a user.

    Args:
        name (str): the name of the user that gets the greeting.
        
    Returns:
        none: does not return anything. 
        
    Notes:
        Made By: Guy Peres
    """
    print(f"hello {name}")
    
def RandonNum(minimum, maximum):
    """return a random integer in the range of min and max entered by user.

    Args:
        minimum (int): minimum value entered by user.
        maximum (int): maximum value entered by user.

    Returns:
        integer: returns an int with a random value between min and max. 
    """
    
    return random.randint(minimum, maximum)

greet("guy")
# help(greet)
print(RandonNum(5, 10))
result = RandonNum(5, 7)
