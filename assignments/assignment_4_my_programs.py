# my_programs.py

def armstrong_number():
    print("Program: Armstrong Number")
    print("""
def is_armstrong(n):
    temp = n
    total = 0
    digits = len(str(n))
    while temp > 0:
        total += (temp % 10) ** digits
        temp //= 10
    return total == n
""")
    print("Test Case 1: is_armstrong(153) -> True")
    print("Test Case 2: is_armstrong(123) -> False")
    print("Explanation: Each digit is raised to the power of total digits and summed. If the sum equals the number, it is an Armstrong number.\n")


def swap_numbers():
    print("Program: Swap Two Numbers")
    print("""
def swap(a, b):
    a, b = b, a
    return a, b
""")
    print("Test Case 1: swap(10, 20) -> (20, 10)")
    print("Test Case 2: swap(-5, 3) -> (3, -5)")
    print("Explanation: Python tuple unpacking swaps values without using a temporary variable.\n")


def count_vowels():
    print("Program: Count Vowels in String")
    print("""
def count_vowels(s):
    vowels = 'aeiouAEIOU'
    count = 0
    for ch in s:
        if ch in vowels:
            count += 1
    return count
""")
    print("Test Case 1: count_vowels('hello') -> 2")
    print("Test Case 2: count_vowels('Python') -> 1")
    print("Explanation: The program checks each character and increments count if it is a vowel.\n")


def gcd_two_numbers():
    print("Program: GCD of Two Numbers")
    print("""
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
""")
    print("Test Case 1: gcd(12, 18) -> 6")
    print("Test Case 2: gcd(7, 3) -> 1")
    print("Explanation: Uses Euclidean algorithm to find the greatest common divisor.\n")


def reverse_number():
    print("Program: Reverse a Number")
    print("""
def reverse_number(n):
    rev = 0
    while n > 0:
        rev = rev * 10 + n % 10
        n //= 10
    return rev
""")
    print("Test Case 1: reverse_number(123) -> 321")
    print("Test Case 2: reverse_number(450) -> 54")
    print("Explanation: Digits are extracted one by one and added in reverse order.\n")


def sum_of_digits():
    print("Program: Sum of Digits")
    print("""
def sum_digits(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total
""")
    print("Test Case 1: sum_digits(123) -> 6")
    print("Test Case 2: sum_digits(908) -> 17")
    print("Explanation: Adds each digit using modulus and integer division.\n")


def count_words():
    print("Program: Count Words in a Sentence")
    print("""
def count_words(s):
    return len(s.split())
""")
    print("Test Case 1: count_words('Hello world') -> 2")
    print("Test Case 2: count_words('Python is easy') -> 3")
    print("Explanation: The split() method divides sentence into words.\n")


def title_case():
    print("Program: Convert String to Title Case")
    print("""
def to_title(s):
    return s.title()
""")
    print("Test Case 1: to_title('hello world') -> 'Hello World'")
    print("Test Case 2: to_title('python programming') -> 'Python Programming'")
    print("Explanation: title() capitalizes the first letter of each word.\n")


def prime_number():
    print("Program: Check Prime Number")
    print("""
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
""")
    print("Test Case 1: is_prime(7) -> True")
    print("Test Case 2: is_prime(10) -> False")
    print("Explanation: Checks divisibility from 2 to n-1.\n")


def factorial():
    print("Program: Factorial of a Number")
    print("""
def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact
""")
    print("Test Case 1: factorial(5) -> 120")
    print("Test Case 2: factorial(3) -> 6")
    print("Explanation: Multiplies numbers from 1 to n.\n")


def fibonacci():
    print("Program: Fibonacci Series")
    print("""
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b
""")
    print("Test Case 1: fibonacci(5) -> 0 1 1 2 3")
    print("Test Case 2: fibonacci(3) -> 0 1 1")
    print("Explanation: Each number is sum of previous two.\n")


def palindrome_string():
    print("Program: Palindrome String")
    print("""
def is_palindrome(s):
    return s == s[::-1]
""")
    print("Test Case 1: is_palindrome('madam') -> True")
    print("Test Case 2: is_palindrome('hello') -> False")
    print("Explanation: Compares string with its reverse.\n")


def custom_sort():
    print("Program: Custom Sorting")
    print("""
def custom_sort(lst):
    return sorted(lst, reverse=True)
""")
    print("Test Case 1: custom_sort([3,1,4]) -> [4,3,1]")
    print("Test Case 2: custom_sort([5,2]) -> [5,2]")
    print("Explanation: Uses sorted() with reverse=True.\n")


def decimal_to_binary():
    print("Program: Decimal to Binary")
    print("""
def dec_to_bin(n):
    return bin(n)[2:]
""")
    print("Test Case 1: dec_to_bin(10) -> 1010")
    print("Test Case 2: dec_to_bin(5) -> 101")
    print("Explanation: bin() converts decimal to binary.\n")


def max_in_list():
    print("Program: Find Maximum in List")
    print("""
def find_max(lst):
    return max(lst)
""")
    print("Test Case 1: find_max([1,5,3]) -> 5")
    print("Test Case 2: find_max([9,2]) -> 9")
    print("Explanation: max() returns the largest element.\n")














    

