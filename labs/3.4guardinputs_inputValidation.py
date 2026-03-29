# def printer(user_input):
#     print(user_input)

# printer("hello")

def process_data_guarded(input):
    if isinstance(input, list):
        if len(input) > 0:
            print(input)
            print(f" you have {len(input)} items in the list")
        else:
            print("no empty lists please!")
    else:
        print(f"you have entered {type(input)} type, instead of list")
        
    
this_list = ["Guy", "Moshe", "Lirone"]
# this_list = []
# process_data_guarded(None)
print(type(None)) #! זה קקה שלא צריך להשתמש בו

# process_data_guarded(this_list)
process_data_guarded(80)