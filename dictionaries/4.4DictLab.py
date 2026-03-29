friend_ages = {
    "Rolf": 24,
    "Adam": 30,
    "Anne": 27
}
# print(f"anne's age is: {friend_ages["Anne"]}")

friend_ages = {
    "Rolf": 24,
    "Adam": 30
}
friend_ages['Bob'] = 20
# print(friend_ages)

friend_ages = {
    "Rolf": 24,
    "Adam": 30
}
friend_ages['Rolf'] = 40
# print(friend_ages["Rolf"])

student_attendance = {
    "Rolf": 96,
    "Bob": 80,
    "Anne": 100
}
# for student in student_attendance:
    # if(student == "Bob"):
        # print(f"I have found bob -> {student}")
    # print(student)

student_attendance = {
    "Rolf": 96,
    "Bob": 80
}
# for student in student_attendance:
    # print(student)
    
student_attendance = {
    "Rolf": 96,
    "Bob": 80
}
for student in student_attendance:
    grade = student_attendance[student]
    # print(f"student name: {student}, grade - {grade}")
    
student_attendance = {
    "Rolf": 96,
    "Bob": 80
}
# for student, grade in student_attendance.items():
    # print(f"student name: {student}, grade - {grade}")
    
student_attendance = {
    "Rolf": 100,
    "Bob": 80,
    "Anne": 60,
    "Guy": 50
}

gradeSum = 0
num_of_students = len(student_attendance)
for student, grade in student_attendance.items():
    gradeSum += grade
# print(f"average of grades is: {gradeSum / num_of_students}")

sum_of_grades = 0
average = sum(student_attendance.values()) / len(student_attendance)
print(f"average of grades for students is: {average}")

friends = [
    {"name": "Rolf", "age": 24},
    {"name": "Adam", "age": 30}
]
# print(friends[1]["name"])

friends = [
    {"name": "Rolf", "age": 24},
    {"name": "Adam", "age": 30},
    {"name": "Anne", "age": 27}
]


result = []

for friend in friends:
    if(friend["age"] > 25):
        result.append(friend)
# print(result)