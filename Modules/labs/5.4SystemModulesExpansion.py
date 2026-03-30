import os
import sys
import subprocess
from pathlib import *
import platform
import random
import time
from collections import Counter
from collections import deque
import hashlib
import calendar
import statistics
import webbrowser
import shutil
import tempfile
import glob



# path = Path("/home/user/file.txt")
# print(f"Path created: {path}")

# print(f"Exists: {path.exists()}")

# print(f"Is file: {path.is_file()}")
# print(f"Is directory: {path.is_dir()}")

# print(f"Random number: {random.randint(1, 10)}")

# items = ['apple', 'banana', 'cherry']
# selected = random.choice(items)
# print(f"Selected: {selected}")

# my_list = [1, 2, 3]
# random.shuffle(my_list)
# print(f"Shuffled list: {my_list}")

# print("Waiting...")
# time.sleep(2)  # מחכה 2 שניות
# print("Done")

# print(time.time()) # ידפיס מספר ארוך כמו 1711800000.0

# data = ['a', 'a', 'a', 'b', 'b']
# counts = Counter(data)
# print(dict(counts)) # פלט: {'a': 3, 'b': 2}

# queue = deque([1, 2, 3])
# first_in = queue.popleft() # מוציא את האיבר הראשון (FIFO)
# print(f"First in: {first_in}")

# text = "hello world"
# # יצירת Hash מסוג md5 (כמו בדוגמה בתמונה)
# hash_object = hashlib.md5(text.encode())
# print(hash_object.hexdigest())

# הדפסת חודש מרץ 2026 (כפי שמופיע בתמונה)
# print(calendar.month(2026, 3))

# data = [1, 5, 9]
# print(f"Mean: {statistics.mean(data)}") # ממוצע: 5

# data = [1, 4, 10]
# print(f"Median: {statistics.median(data)}") # חציון: 4

# webbrowser.open("https://www.google.com")
# print("Browser opened")


# מעתיק את קובץ המקור ליעד חדש
# shutil.copy("source.txt", "destination.txt")
# print("File copied")

# shutil.rmtree("folder_to_delete")
# print("Directory removed")


# יצירת קובץ זמני שנמחק ברגע שסוגרים אותו
# with tempfile.NamedTemporaryFile() as tmp:
#     print(f"Temporary file created at: {tmp.name}")
#     print("Temporary file created")
    

# מחפש את כל הקבצים שמסתיימים בסיומת .py
# files = glob.glob("*.py")
# print(files) # פלט לדוגמה: ['file1.py', 'file2.py']

print("Waiting...")
# השהייה של שנייה אחת
time.sleep(1)

# יצירת מספר אקראי (למשל בין 1 ל-10)
num = random.randint(1, 10)
print(f"Random number: {num}")