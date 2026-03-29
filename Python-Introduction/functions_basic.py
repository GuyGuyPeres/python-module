# Python Functions 
def hello():
    print("Hello World")
    
print(hello)

hello()

print(type(hello))


# Get user age in seconds

def user_age_in_seconds():
    age = int(input("Whats is your age: "))
    age_seconds = age * 365 * 24 * 60 * 60
    print(f"Your age in seconds is: {age_seconds}")

user_age_in_seconds()