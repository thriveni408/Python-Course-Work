# main.py

import my_programs

while True:
    print("\n------ FUNCTION MENU ------")
    print("1. Armstrong Number")
    print("2. Swap Two Numbers")
    print("3. Count Vowels in String")
    print("4. GCD of Two Numbers")
    print("5. Reverse a Number")
    print("6. Sum of Digits")
    print("7. Count Words")
    print("8. Title Case Conversion")
    print("9. Prime Number")
    print("10. Factorial")
    print("11. Fibonacci Series")
    print("12. Palindrome String")
    print("13. Custom Sorting")
    print("14. Decimal to Binary")
    print("15. Maximum in List")
    print("0. Exit")
    print("----------------------------")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        my_programs.armstrong_number()
    elif choice == 2:
        my_programs.swap_numbers()
    elif choice == 3:
        my_programs.count_vowels()
    elif choice == 4:
        my_programs.gcd_two_numbers()
    elif choice == 5:
        my_programs.reverse_number()
    elif choice == 6:
        my_programs.sum_of_digits()
    elif choice == 7:
        my_programs.count_words()
    elif choice == 8:
        my_programs.title_case()
    elif choice == 9:
        my_programs.prime_number()
    elif choice == 10:
        my_programs.factorial()
    elif choice == 11:
        my_programs.fibonacci()
    elif choice == 12:
        my_programs.palindrome_string()
    elif choice == 13:
        my_programs.custom_sort()
    elif choice == 14:
        my_programs.decimal_to_binary()
    elif choice == 15:
        my_programs.max_in_list()
    elif choice == 0:
        print("Exiting program. Thank you!")
        break
    else:
        print("Invalid choice! Please try again.")
