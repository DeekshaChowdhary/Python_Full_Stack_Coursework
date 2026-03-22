# --------------------------- ATM SYSTEM (PYTHON) ---------------------------

"""
---------Features-----------:
- Check Balance
- Deposit Money
- Withdraw Money
- View Transaction History
- Change PIN

----------Notes-------------:
- Dictionary is used to store account details
- Keys are account numbers
- Values contain PIN, balance, and transaction history
"""


# --------------------------- DATABASE ---------------------------

data = {
    '123456': {'pin': '1234', 'balance': 4000, 'history': []},
    '223456': {'pin': '1234', 'balance': 5000, 'history': []},
    '333456': {'pin': '1234', 'balance': 6000, 'history': []},
    '444456': {'pin': '1234', 'balance': 7000, 'history': []},
}


# --------------------------- FUNCTIONS ---------------------------

def deposit(acc_num):
    """Deposit money into account"""
    amount = int(input("Enter the amount: "))
    data[acc_num]['balance'] += amount
    data[acc_num]['history'].append(f"{amount} deposited")

    print(f"{amount} deposited successfully")
    check_balance(acc_num)


def withdraw(acc_num):
    """Withdraw money from account"""
    amount = int(input("Enter the amount: "))

    if data[acc_num]['balance'] >= amount:
        data[acc_num]['balance'] -= amount
        data[acc_num]['history'].append(f"{amount} withdrawn")

        print(f"{amount} withdrawn successfully")
        check_balance(acc_num)
    else:
        print("Insufficient balance")


def change_pin(acc_num):
    """Change account PIN"""
    old_pin = input("Enter your old PIN: ")

    if old_pin == data[acc_num]['pin']:
        new_pin = input("Enter new PIN: ")
        data[acc_num]['pin'] = new_pin
        print("PIN updated successfully")
    else:
        print("Incorrect PIN")


def check_balance(acc_num):
    """Display account balance"""
    print(f"Current Balance: {data[acc_num]['balance']}")


def view_transaction(acc_num):
    """Display transaction history"""
    history = data[acc_num]['history']

    if history:
        print("\n------ Transaction History ------")
        for txn in history:
            print(txn)
        print("------ End of Transactions ------\n")
    else:
        print("No transactions found")


def menu():
    """Display ATM menu"""
    print("\n--------- ATM MENU ---------")
    print("[C] Check Balance")
    print("[D] Deposit")
    print("[W] Withdraw")
    print("[V] View Transactions")
    print("[P] Change PIN")
    print("[E] Exit")


# --------------------------- MAIN PROGRAM ---------------------------

print("------------- Welcome to ATM System -------------------")

acc_num = input("Enter account number: ")
pin = input("Enter PIN: ")

# Login validation
if acc_num in data and data[acc_num]['pin'] == pin:
    print("Login Successful")

    while True:
        menu()
        choice = input("Enter your choice: ").lower()

        if choice == 'c':
            check_balance(acc_num)

        elif choice == 'd':
            deposit(acc_num)

        elif choice == 'w':
            withdraw(acc_num)

        elif choice == 'v':
            view_transaction(acc_num)

        elif choice == 'p':
            change_pin(acc_num)

        elif choice == 'e':
            print("Thank you for using ATM")
            break

        else:
            print("Invalid choice. Please try again.")

else:
    print("Invalid login credentials")
