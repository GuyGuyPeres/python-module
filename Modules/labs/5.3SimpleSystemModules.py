import os
import sys
# import subprocess
# import pathlib
# import platform



# print(os.name)

# print(os.getcwd())

# files = os.listdir('.')
# for file in files:
#     print(file)

# os.mkdir("thats_a_folder")

# os.rmdir("thats_a_folder")
# print("Folder deleted")

# os.chdir("thats_a_folder")

# with open("test_file.txt", 'w') as f:
#     pass
# print('file created')

# exists = os.path.exists("test_file.txt")
# print(exists) # ידפיס True

# os.remove("test_file.txt")
# print("File deleted")

# print(f"name of the script: {sys.argv[0]}")
# print(f"Argument received: {sys.argv[1]}")
# print(f"Total arguments: {len(sys.argv)}")
# print(sys.argv)

# print("Program terminated")
# sys.exit()
# כל קוד שייכתב כאן לא יתבצע

# path_value = os.environ.get("PATH")
# print(f"PATH={path_value}") # מציג רק את ההתחלה לפי הפלט בתמונה

# if sys.platform.startswith('linux'):
#     print("Running on Linux")
# elif sys.platform.startswith('win'):
#     print("Running on Windows")
# print(sys.platform)    

# path = os.path.join("home", "user", "test", "file.txt")
# print(path)

# path = "5.5TkinterExerciseLab.py" # או כל נתיב אחר
# if os.path.isdir(path):
#     print("This is a directory")
# elif os.path.isfile(path):
#     print("This is a file")
    
# הרצת פקודת ls (מתאים ללינוקס) -- > בטרמינל
# os.system("ls")

# 1. צור תיקייה
# folder = "final_task"
# if not os.path.exists(folder):
#     os.mkdir(folder)
#     print("Folder created")


# # 2. צור קובץ בתוך התיקייה
# file_path = os.path.join(folder, "task.txt")
# with open(file_path, 'w') as f:
#     f.write("Done!")
# print("File created")

# # 3. בדוק קיום
# print(os.path.exists(file_path))

# # 4. מחק הכל (Cleanup)
# os.remove(file_path)
# os.rmdir(folder)
# print("Cleanup done")

