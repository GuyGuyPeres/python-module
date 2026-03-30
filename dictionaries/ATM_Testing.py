user_account = {
    "account_id": 1001,
    "username": "Yuval",
    "balance": 55000,
    "pin": 3571
}

def auth():
    pin = int(input("enter your PIN: "))
    return pin

def withdraw():
    user_pin = auth()
    if user_pin == user_account["pin"]:
        amount = float(input("Please type the amount you would like to withdraw: "))
        if amount > user_account["balance"]:
            print("You are poor")
        else:
            user_account["balance"] -= amount
            print(f"Your Balance now is {user_account["balance"]}")
    else:
        print("Wrong PIN, goodbye")
        exit()

def deposite():
    print("This is the deposite logic")
    pass

def balance():
    print("This is the balance logic")
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
    