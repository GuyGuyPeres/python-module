user_account = {
    "account_id": 1001,
    "username": "Yuval",
    "balance": 55000,
    "pin": 3571
}

def auth(account_pin):
    pin = int(input("enter your PIN: "))
    if account_pin == pin:
        return True
    else:
        return False
        

def withdraw():
    if auth(user_account["pin"]):
        amount = float(input("Please type the amount you would like to withdraw: "))
        if amount > user_account["balance"]:
            print("You are poor")
        else:
            user_account["balance"] -= amount
            balance()
    else:
        print("Wrong PIN, goodbye")
        exit()

def deposite():
    if auth(user_account["pin"]):
        amount = float(input("Please type the amount you would like to deposite: "))
        if amount < 0:
            print("You cannot tpye negative numbers")
            exit()
        else:
            user_account["balance"] += amount
            balance()
    else:
        print("Wrong PIN, goodbye")
        exit()

def balance():
    print(f"Your Balance now is {user_account["balance"]}")
    pass


while True:
    print("======= Welcome to Python ATM =======")    
    user_choise = int(input("""
        Choose one: 
        1. withdraw Money
        2. Deposite Money
        3. Balance
        0. to exit
    """))
    
    # print(f"User Choosed {user_choise}")
    
    match user_choise:
        case 1:
            withdraw()
        case 2:
            deposite()
        case 3:
            balance()
        case 0:
            print("Ok, Exiting...")
            exit()
    