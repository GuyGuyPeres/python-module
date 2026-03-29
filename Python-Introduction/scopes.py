# python scope:
list1 = ["a", "b", "c"]
print(list1)

# 1st way - func1 will fail
def func1():
    list1 = list1 + ["d", "e", "f"]
# func1()
print(list1)

# 2nd way - will work
def func2():
    global list1
    list1 = list1 + ["d", "e", "f"]
func2()
print(list1)

# 3rd way - will work append:
def func3():
    list1.append(["h", "i", "j"])
func3()
print(list1)

# 4th way - will work extend
def func4():
    list1.extend(["k", "l"])
func4()
print(list1)

# explain:
# func1 failed - because inside function we dont know the global variable list1.
# func2 - we said "global list1" - so python knows to search outside function.
# func3, func4 - we use append and extend - so python automatically know to search outside function for global var.
# append - add another inner list.
# extend - add the elements to the original list - 1 by 1.