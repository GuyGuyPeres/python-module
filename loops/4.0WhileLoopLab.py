
i = 1; 

while i < 6:
    # print(i)
    i += 1
    
i = 5; 

while i > 0:
    # print(i)
    i -= 1
    
# i = 0
# while i < 10:
#     if(i % 2 == 0):
#         print(i)
#     i += 1

counter = 0
i = 1
while i < 6:
    counter = counter + i
    # print(counter)
    # print(i)
    i += 1
    
# i = 0
# while i < 10:
#     if(i % 3 == 0):
#         print(i)
#     i += 1

# i = 0
# user_input = int(input("please enter a number: "))
# while i < 5:
#     print(user_input)
#     i += 1

# i = 1
# user_input = int(input("please enter a number: "))
# while i < user_input + 1:
#     print(i)
#     i += 1

# user_input = 1
# while user_input != 0:
#     user_input = int(input("please enter a '0': "))
# print("thanks for writing '0' ")

# password = 1234
# user_input = 0
# while user_input != password:
#     user_input = int(input("please enter your password - hint >'12...': "))
# print("thanks for writing '1234' ")

# user_input = input("please write 'y' if you wish to continue or 'n' if not: ")
# while user_input == "y":
#     print("app in running")
#     user_input = input("please write 'y' if you wish to continue or 'n' if not:")
# print("you chose to leave (n)")

# i = 0
# while i < 10:
#     if(i % 2 == 0):
#         print(i)
#     i += 1

# counter = 0
# i = 1
# while i < 21:
#     if(i % 2 == 0):
#         counter += 1
#         print(i)
#     i += 1
# print(f"there are {counter} even numbers until 20")

counter_sum = 0
i = 1
while i < 11:
    if(i % 2 != 0):
        counter_sum += i
        print(i)
    i += 1
print(counter_sum)