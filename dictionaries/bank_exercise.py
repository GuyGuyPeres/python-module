
accounts = [
    {"account_id": 100, "name": "Liron", "pin": "1234", "balance": 1000},
    {"account_id": 101, "name": "Daniel", "pin": "5678", "balance": 500},
    {"account_id": 102, "name": "Guy", "pin": "1122", "balance": 2000},
    {"account_id": 103, "name": "Moshe", "pin": "0987", "balance": 700}
]

ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "admin1234"

def admin_login():
    username = input("admin username: ")
    password = input("admin password: ")
    if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
        print("---Hello Admin---")
        return True
    
    print("Access denied")
    return False

def create_account():
    if not admin_login():
        return

    name = input("Enter name: ")
    pin = input("Set PIN: ")

    account = {
        "account_id": len(accounts) + 100,
        "name": name,
        "pin": pin,
        "balance": 0
    }

    accounts.append(account)

def find_account(account_id_input):
    for account in accounts:
        if account["account_id"] == account_id_input:
            return account
    print("could not find the account")
    return None

def verify_pin(account, pin_input):
    if pin_input == account["pin"]:
        return True
    

def deposit():
    account_id = int(input("enter account ID: "))
    pin = input("enter pin: ")
    amount = float(input("enter amount to deposit: "))
    
    account = find_account(account_id)
    
    if not account:
        print("account not found!")
        return
    
    if not verify_pin(account, pin):
        print("wrong pin!!!")
        return
    
    if amount <= 0:
        print("invalid amount")
        return
    
    account["balance"] += amount

def withdraw():
    account_id = int(input("Account ID: "))
    pin = input("PIN: ")
    amount = float(input("Amount: "))

    account = find_account(account_id)

    if not account:
        print("Account not found")
        return

    if not verify_pin(account, pin):
        print("Wrong PIN")
        return

    if account["balance"] < amount:
        print("Insufficient funds - Work Harder.")
        return

    account["balance"] -= amount

def show_account():
    account_id = int(input("Account ID: "))
    pin = input("PIN: ")

    account = find_account(account_id)

    if not account:
        print("Account not found")
        return

    if not verify_pin(account, pin):
        print("Wrong PIN")
        return

    print(account)

def view_all_accounts():

    if not admin_login():
        return

    for account in accounts:
        print(account)


while True:
    # print("Welcome to the ATM machine App")
    # print("--------------------------------")
    print("1.Create 2.Deposit 3.Withdraw 4.Show 5.Admin View 6.Exit")

    choice = input("Choose: ")

    if choice == "1":
        create_account()

    elif choice == "2":
        deposit()

    elif choice == "3":
        withdraw()

    elif choice == "4":
        show_account()

    elif choice == "5":
        view_all_accounts()

    elif choice == "6":
        break