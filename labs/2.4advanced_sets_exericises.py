# print(set([[1, 2], [3, 4]])) # ----> #!TYPEERROR - אי אפשר לשים ליסט או סט בתוך סט

set_of_tuples = {(1, 2), (3, 4)}
# print(set_of_tuples)
# print((1, 2) in set_of_tuples) #---> True

developers = {"Alice", "Bob", "Charlie"}
admins = {"Alice", "David"}

# מחברים בין הסטים
# print(developers.union(admins))
# print(developers | admins)

# בודק מה המשותפים
# print(developers.intersection(admins))
# print(developers & admins)

#בודק מה מהראשון לא קיים בשני 
# print(developers.difference(admins))
# print(developers - admins)

# developers.intersection_update(admins) #---> מעדכן בלייב את הסט
# print(developers)




