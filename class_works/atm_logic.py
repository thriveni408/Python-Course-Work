user_data = ("123456", "7890")  

account_details = {
    "balance": 5000.00,
    "transactions": []
}

operations = (
    "1. Check Balance",
    "2. Deposit",
    "3. Withdraw",
    "4. View Transactions",
    "5. Exit"
)


def login(account_input, pin_input):
    if (account_input, pin_input) != user_data:
        print("Incorrect account number or PIN")
        return False
    print("\nLogin Successful")
    return True


def display_menu():
    print("\nATM MENU")
    for op in operations:
        print(op)


def check_balance():
    print("\nCurrent Balance: ₹", format(account_details["balance"], ".2f"))


def deposit_money():
    deposit_amount =  int(input("\nEnter amount to deposit: "))
    if deposit_amount > 0:
        account_details["balance"] += deposit_amount
        account_details["transactions"].append(f"Deposited ₹{deposit_amount:.2f}")
        print("Successfully deposited ₹", format(deposit_amount, ".2f"))
    else:
        print("Invalid deposit amount")
   
def withdraw_money():
    withdraw_amount = int(input("\nEnter amount to withdraw: "))
    if 0 < withdraw_amount <= account_details["balance"]:
        account_details["balance"] -= withdraw_amount
        account_details["transactions"].append(f"Withdrawn ₹{withdraw_amount:.2f}")
        print("Successfully withdrawn ₹", format(withdraw_amount, ".2f"))
    else:
        print("Insufficient balance or invalid amount")


def show_transactions():
    print("\nTransaction History:")
    if account_details["transactions"]:
        for txn in account_details["transactions"]:
            print("-", txn)
    else:
        print("No transactions yet")
        
        
        
        
        






