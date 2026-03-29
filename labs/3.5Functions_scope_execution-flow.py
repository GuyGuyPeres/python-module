def AskForAge():
    user_age = int(input("Enter you age please: "))
    print(f"you age is {user_age}")
    age_seconds = 365 * user_age * 24 * 60 * 60
    print(f"your age in seconds is {age_seconds} seconds")

# AskForAge()


global this_list
this_list = ["Guy", "Moshe", "Lirone"]

def add_to_list(friend_name):
    this_list.append(friend_name)
    print(this_list) 
    
add_to_list("yosi")
add_to_list("yosi2")
add_to_list("yosi3")

