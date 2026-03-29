number_int = 6 # Integer
number_float = 6.0 # Float
string = "Baba" # String
boolers = False # Boolean (0)
boolers = True # Boolean (1)


# List
book1 = "Harry Potter - and the Philosopher's Stone"
book2 = "Harry Potter - and the Chamber of Secrets"
book3 = "Harry Potter - and the Prisoner of Azkaban"
book4 = "Harry Potter - and the Goblet of Fire"
book5 = "Harry Potter - and the Order of the Phoenix"
book6 = "Harry Potter - and the Half-Blood Prince"
book7 = "Harry Potter - and the Deathly Hallows"

harry_potter_books = [
    "Harry Potter - and the Philosopher's Stone", # idx 0
    "Harry Potter - and the Chamber of Secrets", # idx 1
    "Harry Potter - and the Prisoner of Azkaban", # idx 2
    "Harry Potter - and the Goblet of Fire", # idx 3 
    "Harry Potter - and the Order of the Phoenix",# idx 4
    "Harry Potter - and the Half-Blood Prince", # idx 5
    "Harry Potter - and the Deathly Hallows" # idx 6
]

# print(harry_potter_books)
# print(harry_potter_books[3])

# List 
my_list = ["Bob", "Rolf", "Anne"]
# print(my_list[1])
# print(my_list)

# Tuple
my_tuple = ("Bob", "Rolf", "Anne")
# print(my_tuple[1])
# print(my_tuple)

# Set
my_set = {"Bob", "Rolf", "Anne"}
# print(my_set[1]) #!----> cant print > not ordered
# print(my_set)

name = "Mickey"
# name[0] = "S" #! Expect to get Sickey but wont work cause strings are immutable


my_list = ["Bob", "Rolf", "Anne"]
# print(my_list)
my_list[0] = "Smith"
# print(my_list)

my_servers = [
    "1us-east-1",
    "2us-west-1",
    "3eu-west-1",
    "4il-west-1",
    "5il-central-1",
    "6us-north-1",
    "7il-south-1"
    
]
# print(my_servers)

# print(my_servers[-1]) #---> איבר אחרון בעזרת אינדקס שלילי

# print(my_servers[0:3]) #---> מדפיס בסלייסינג לא כולל האחרון

# print(my_servers[0:-2]) #---> מדפיס בסלייסינג עם שליליים

# print(my_servers[0:7:2]) #---> מדפיס בסלייסינג עם קפיצות של 2

mixed_list = [
    "Mister",
    True,
    "Shmister",
    123,
    False,
    "Guy"
]
# print(mixed_list)

mixed_list.append("I have been added")
# print(mixed_list)

deployment_targets = [
    "us-east-1",
    "eu-west-1",
    "ap-southeast-1"
]
# print(deployment_targets)
# print(deployment_targets[0])

deployment_targets.append("us-west-2")
# print(deployment_targets)
deployment_targets.append("us-north-3")
# print(deployment_targets)
deployment_targets[1] = "eu-central-1"
# print(deployment_targets)
# print(len(deployment_targets))

new_tuple2 = ("guy", "moshe", "dan", 123)
# print(new_tuple2)
# print(len(new_tuple2))
# print(new_tuple2[0:-1])

host_port = ("127.0.0.1", "3000")
# print(host_port)
# print(type(host_port))

red_rgb = (255, 0, 0)
# print(red_rgb[0])
single_value = (1)
# print(type(single_value))
single_value = (1,)
# print(type(single_value))

# print(host_port[:1])
# print(host_port[-2:])
# print(f"IP: {host_port[0]} PORT: {host_port[1]}")

ports_list = [
    8080,
    8443,
    22,
    8080,
    443
]

unique_ports = set(ports_list)
print(unique_ports)

server_names = {
    "web01",
    "web02",
    "web03"
}

# if 22 in unique_ports:
#     print(True)
# else:
#     print(False)
    
# if 22 in server_names:
#     print(True)
# else:
#     print(f"not in server names, {False}")
    
unique_ports.add(3000)
# print(unique_ports)

# unique_ports.remove(22) #---> מוציא שגיאה אם האלמנט לא נמצא בסט
# unique_ports.discard(22) #---> לא מוציא שגיאה אם האלמנט לא קיים בסט
# print(unique_ports)

valid_set = { #?----> cant not make set with list, But can make set with tuple
    (1, 2),
    (3, 4)
}

my_list2 = [1, 1, 2, 2, 3, 4, 5]
# print(my_list2)
my_set2 = set(my_list2) #---> removes duplicates when made set
# print(my_set2) 
my_set2.add("AddedThisElement")
# print(my_set2) 

#------------------------------------------------------------------

s = {"write","execute","read", "read"}
l = ["write","execute","read", "read"]
# print(type(l[1]))

# Set are more restricted then tupples
#! This will raise an error because lists are mutable and cannot be added to a set
# set_of_lists = {{"write","execute"}, {"read", "read"}} 

set_of_tuples = {(1, 2), (3, 4)}
# print(set_of_tuples)
# print("doron" in s)

developers = {"Alice", "Bob", "Charlie"}
admins = {"Alice", "David"}

# print("Is alice in developres team?", "Alice" in developers)
# print("Is alice in admins team?", "Alice" in admins)

# ===============================

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.union(y)

# print(z)

# ==============================

all_members = developers.union(admins)
# print(all_members)

# ==============================
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)

# print(z)

# ==============================
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.difference(y) 
w = y.difference(x) 

# print(z)
# print(w)



