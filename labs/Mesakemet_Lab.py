# ====================================
#     My Profile App - 22/03/2026
# ====================================

print("--- Welcome To The App Profile Page! ---")
name = input("enter your name: ")
age = input("Enter your age: ")
city = input("Enter your city: ")

hobbies = input('Type your 3 hobbies, use "," after every hobbie: ').split(",") #? users should type "gaming,footbal,food" => ["gaming", "football", "food"]
# print(type(hobbies))
popular_hobbies = ["music", "sports", "gaming", "reading"]

print(f"Hello {name},\nage: {age} from {city}\nyour hobbies are: {", ".join(hobbies)}")
# print(hobbies)
# common_popular_hobbies = set(hobbies).intersection(set(popular_hobbies))

for hobbie in hobbies:
    if hobbie in popular_hobbies:
        print(f"{hobbie} is in popular hobbies! TRUE")
    else:
        print(f"{hobbie} is NOT in popular hobbies! FALSE")

unique_set_hobbies = set(hobbies).difference(set(popular_hobbies))
print(f"your unique hobbies are: {", ".join(unique_set_hobbies)}")

numOfhobbies = 0
for hobbie in hobbies:
    numOfhobbies += 1

numOfUniqueHobbies = 0
for unique_hobbie in unique_set_hobbies:
    numOfUniqueHobbies += 1


print(f"Hello {name}, Your Number of Hobbies: {numOfhobbies}")
print(f"Hello {name}, Number of UNIQUE Hobbies: {numOfUniqueHobbies}")

hobbies_tuple = tuple(hobbies)

if "music" in hobbies_tuple:
    print(f"music is in USERS hobbies list")
else:
    print(f"music is not in USERS hobbies list")