# The Boolean DataType has only two available oiptions
# True
# False

is_adult = True
print(type(is_adult))
print(is_adult)

# =========

# Comparaisons
print(5 == 5)
print("Baba" == "baba")
print(5 > 10)

print(10 != 10)
print(10 != 8)

# More Operators
print(5 < 10) # True
print(10 >= 10) # True
print(9 <= 10) # True

# comapring lists
friends = ["Bob", "Rolf", "Anne"]
abroad = ["Bob", "Anne", "Rolf"]

print(set(friends) == set(abroad))

# "==" or "is"
print(friends[1] is abroad[2])

# if
# elif
# else

day_of_week = input("What day of week is it today? ").lower()
# print(day_of_week == "monday")

if day_of_week == "monday":
    print("Have a great start of week!")
elif day_of_week == "tuesday":
    print("It's a productive Tuesday")
else: 
    print("Full speed ahead")

print("This always runs.")
