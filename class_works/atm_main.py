import ATM_logic

account_number = input("Enter the account_number: ")
pin = input("Enter the pin: ")

if ATM_logic.login(account_number, pin):
    while True:
        ATM_logic.display_menu()
        ch = int(input("Enter the choice: "))

        if ch == 1:
            ATM_logic.check_balance()
        elif ch == 2:
            ATM_logic.deposit_money()
        elif ch == 3:
            ATM_logic.withdraw_money()
        elif ch == 4:
            ATM_logic.show_transactions()
        elif ch == 5:
            print("Thank you, Bye!!!!")
            break
        else:
            print("Enter a valid choice")
