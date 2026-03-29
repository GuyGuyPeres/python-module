movies_set = {"baywatch", "1917", "dracula", "1917"}
# user_movie = input("enter a movie name: ").lower()

# if user_movie in movies_set:
#     print("that movie is in the set")
# else:
#     print("that movie is NOT in the set")
    
NumToGuess = 8
answer_tuple = ("Y", "y", "yes", "YES", "Yes")

user_input = input("enter Yes or Y if you want to play: ") #--> אפשר פשוט לבחור שיהיה באותיות גדולות או קטנות לנוחיות

if user_input in answer_tuple:
    print("you chose YES, please enter then number to guess now \n")
    user_num = int(input("enter your number here: "))
    if user_num == NumToGuess:
        print(f"number is correct! good choice! num is {NumToGuess}")
    else:
        print("this is the wrong number! \n")
        if abs(NumToGuess - user_num) > 1:
            print("you are NOT close")
        elif abs(NumToGuess - user_num) == 1:
            print("you are off by one")
else:
    print("you chose NOT to play")