def TakeList_GiveTuple(list):
    NumCounter = 0
    NumSum = 0
    for number in list:
        NumCounter += 1
        NumSum = NumSum + number  
        NumAverage = NumSum / NumCounter  
        NumTuple = ()
    print(f"number of nums in list is: {NumCounter}")
    print(f"Sum of number un the list is: {NumSum}")
    print(f"Average of the numbers in the list is: {NumAverage}")
    NumTuple += (NumCounter,)
    NumTuple += (NumSum,)
    NumTuple += (NumCounter,)
    print(NumTuple)
    
    
def giveBiggest_giveLowest(list):
    biggestNum = list[0]
    lowestNum = list[0]
    big_small_tuple = ()
    for number in list:
        if number > biggestNum:
            biggestNum = number
            
        if number < lowestNum:
            lowestNum = number
            # print(lowestNum)
            
    big_small_tuple += (lowestNum,)
    big_small_tuple += (biggestNum,)
    print(f"lowest: {lowestNum}, biggest: {biggestNum}")
    print(big_small_tuple)

def even_nums(list):
    Even_list = []
    for number in list:
        if number % 2 == 0:
            Even_list.append(number)
    print(Even_list)
    return(Even_list)

def tziunAbove60(list):
    Above60List = []
    for tziun in list:
        if tziun > 60:
            Above60List.append(tziun)
    print(Above60List)
            
def empty_or_average(list):
    NumSum = 0
    NumCounter = 0
    if len(list) == 0:
        print("this shit is empty")
        return(None)
    else:
        for number in list:
            NumCounter += 1
            NumSum = NumSum + number
        print(f"average is: {NumSum / NumCounter}")
        return(NumSum / NumCounter)

def reverse_this_list(list_input, reverse_input):
    if reverse_input == True:
        randomList = list_input
        randomList.reverse()
        print(randomList)
    
def return_biggest_num(*numbers):
    biggest_list = numbers
    biggest_num = biggest_list[0]
    for number in numbers:
        if number > biggest_num:
            biggest_num = number
    print(f"biggest number is: {biggest_num}")
    
def even_nums_advanced(*random_numbers):
    random_numbers_list = random_numbers
    Even_list = []
    for number in random_numbers_list:
        if number % 2 == 0:
            Even_list.append(number)
    print(Even_list)
    return(Even_list)

def SumNestedFunction(list):
    def sumNested(list):
        sumNumber = 0
        for number in list:
            sumNumber = sumNumber + number
        print(f"the sum in nested func is: {sumNumber}")
        return(sumNumber)
    sumNested(list)
    
    
    
global thisvar
thisvar = 3

def varOutside_funcNested():
    def nestedFunc():
        var_inside = thisvar
        print(f"accesed successfully - {var_inside}")
    nestedFunc()

def nonLocal_var_func():
    this_var_is_important = "Outer Function"
    def this_func_nested():
        nonlocal this_var_is_important
        this_var_is_important = "Inside Function"
        print(this_var_is_important)
    print(this_var_is_important)
    this_func_nested()
    
def AddOne(item):
    item += 1
    return(item)

def getList_DoSomethingTo_EveryItem(list, function):
    new_list = []
    for item in list:
        
        new_list.append(function(item))
    print(new_list)


def tuple_odd_even(list):
    oddList = []
    evenList = []
    for item in list:
        if item % 2 == 0:
            evenList.append(item)
        else:
            oddList.append(item)
    print(f"odd list: {oddList}")
    print(f"even list: {evenList}")
    
    

        
    
    

this_list = [20, 100, 30, 50, 1000, 2, 10, 700] #---> all is even
this_list2 =[7, 10, 2, 20 ,100 ,101, 29, 9,1003]
this_list3 =[1, 2, 3, 4, 5, 6, 7, 8]
this_list4=[]
# TakeList_GiveTuple(this_list)
# giveBiggest_giveLowest(this_list)
# even_nums(this_list2)
# tziunAbove60(this_list)
# empty_or_average(this_list4)
# reverse_this_list(this_list, True)
# return_biggest_num(0, 100, 3, 1000, 3, 200, 2000)
# even_nums_advanced(1, 2, 3, 100, 102, 217, 7, 9, 1006)
# SumNestedFunction(this_list3)
# varOutside_funcNested()
# nonLocal_var_func()
# getList_DoSomethingTo_EveryItem(this_list3, AddOne)
tuple_odd_even(this_list2)