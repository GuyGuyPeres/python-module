friends = ["Jen", "Bob", "Rolf"]
print("Jen" in friends)

movies_set = {"baywatch", "1917", "dracula", "1917"}
user_movie = input("enter a movie name: ").lower()

print(user_movie in movies_set)

print("17" in "1917") # => True

if user_movie in movies_set:
    print(f"{user_movie} is a very nice movie in is on the list")
else:
    print(f"that movie is not on the list")