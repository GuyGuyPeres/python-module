def do_nothing(x, y):
    pass

def do_something(x, y):
    print(x + y)
    
def give_name(name):
    print(name)
    
    
def give_2names(firstname, lastname):
    print(f"{firstname} {lastname}")

def divide_two_numbers(num1, num2):
   if num1 == 0 or num2 == 0:
       print("YOU FOOL!")
   else:
        print(num1 / num2)
       
    

# do_something(5, 100)
# give_name("guy")
# divide_two_numbers(0, 10)
give_2names(lastname="guy", firstname="peres")
give_2names("guy", lastname="peres")
# give_2names(lastname="guy", "peres") #--> positional argument cannot appear after keyword argument
give_2names("moshe", "aharonson")