from datetime import date
from datetime import datetime
from datetime import timedelta
import math

print(date.today())

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print(current_time)

year_only = date.today().year
print(year_only)

# UserAge = int(input("enter your age: "))
# print(UserAge - year_only)

def calculate_end_of_year():
    # הגדרת התאריך של היום
    today = date.today()

# הגדרת היום האחרון של השנה הנוכחית
    end_of_year = date(today.year, 12, 31)

# חישוב ההפרש בין התאריכים
    remaining = end_of_year - today

# הדפסת התוצאה (שימוש ב- .days כדי לקבל רק את מספר הימים)
    print(f"Days left: {remaining.days}")
    
# calculate_end_of_year()

# הדפסת השם המלא של היום בשבוע
print(datetime.now().strftime("%A"))

def add_10_days():
    # הגדרת התאריך של היום
    today = date.today()

# יצירת פרק זמן של 10 ימים
    ten_days = timedelta(days=10)

# חישוב התאריך העתידי
    future_date = today + ten_days

    print(f"Future date: {future_date}")
# add_10_days()

def calculate_time_between_days():
    # הגדרת שני תאריכים (לדוגמה: ה-10 באפריל וה-5 באפריל)
    date1 = date(2026, 4, 10)
    date2 = date(2026, 4, 5)

    # חישוב ההפרש
    delta = date1 - date2

    # הדפסת התוצאה
    print(f"Difference: {delta}")
    
# calculate_time_between_days()

def readable_format():
    # קבלת הזמן הנוכחי
    now = datetime.now()

    # עיצוב הזמן לפי התבנית: יום/חודש/שנה שעה:דקה
    formatted_time = now.strftime("%d/%m/%Y %H:%M")

    print(formatted_time)
# readable_format()

def check_saturday_sunday():
    # קבלת היום הנוכחי
    today = date.today()

    # בדיקה האם היום הוא שבת (5) או ראשון (6)
    is_weekend = today.weekday() >= 5

    # הדפסת התוצאה בפורמט המבוקש
    print(f"Weekend: {is_weekend}")
# check_saturday_sunday()

def shoresh():
    # הגדרת המספר
    number = 16

    # חישוב השורש הריבועי
    result = math.sqrt(number)

    # הדפסת התוצאה בפורמט המבוקש
    print(f"√{number} = {result}")
# shoresh()

def hours_from_start_of_the_day():
    # 1. קבלת הזמן הנוכחי
    now = datetime.now()

    # 2. שליפת מספר השעות שעברו מתחילת היום (0-23)
    hours_passed = now.hour

    # 3. הכפלה ב-2
    result = hours_passed * 2

    # 4. הדפסת התוצאה
    print(f"Result = {result}")