# -----------------------------------------
# Basic input examples
# -----------------------------------------

name = input("Enter the name: ")
print("Name:", name)

age = int(input("Enter the age: "))
print("Age:", age)

discount = float(input("Enter the discount: "))
print("Discount:", discount)

# -----------------------------------------
# Input as string
# -----------------------------------------

names = input("Enter names (space-separated): ")
print("Names string:", names)

# -----------------------------------------
# Input → list of strings
# -----------------------------------------

names = input("Enter words: ").split()
print("List of strings:", names)

# -----------------------------------------
# Input → list of integers
# -----------------------------------------

nums = list(map(int, input("Enter integers: ").split()))
print("List of integers:", nums)

# -----------------------------------------
# Input → list of floats
# -----------------------------------------

floats = list(map(float, input("Enter floats: ").split()))
print("List of floats:", floats)

# -----------------------------------------
# Input → tuple of strings
# -----------------------------------------

tup1 = tuple(input("Enter words: ").split())
print("Tuple of strings:", tup1)

# -----------------------------------------
# Input → tuple of integers
# -----------------------------------------

tup2 = tuple(map(int, input("Enter integers: ").split()))
print("Tuple of integers:", tup2)

# -----------------------------------------
# Input → tuple of floats
# -----------------------------------------

tup3 = tuple(map(float, input("Enter floats: ").split()))
print("Tuple of floats:", tup3)

# -----------------------------------------
# Input → set of integers / floats / strings
# -----------------------------------------

s1 = set(map(int, input("Enter integers for set: ").split()))
print("Set of integers:", s1)

s2 = set(map(float, input("Enter floats for set: ").split()))
print("Set of floats:", s2)

s3 = set(input("Enter words for set: ").split())
print("Set of strings:", s3)

# -----------------------------------------
# Using eval (useful for dict, list, tuple, string etc.)
# -----------------------------------------

data = eval(input("Enter any Python object (list/dict/tuple/string): "))
print("Eval output:", data)

# -----------------------------------------
# Unpacking examples
# -----------------------------------------

s = input("Enter username and email: ").split()
a, b = s
print("Username:", a)
print("Email:", b)

name, email = input("Enter name and email: ").split()
print("Name:", name)
print("Email:", email)

# -----------------------------------------
# Multiple values input
# -----------------------------------------

a, b = map(int, input("Enter two numbers: ").split())
print("a:", a)
print("b:", b)

# -----------------------------------------
# Variable unpacking (no input)
# -----------------------------------------

a, b, c = 10, 20, 30
print("a =", a, "b =", b, "c =", c)

print("a =", a, "\nb =", b, "\nc =", c)
print("a =", a, "\tb =", b, "\tc =", c)
print("a=", a, "\tb=", b, "\tc=", c, sep='')
print("a=", a, "\tb=", b, "\tc=", c, sep='\t\t')

print("a=", a, "b=", b, "c=", c, end="\n\n\n")

# -----------------------------------------
# f-strings
# -----------------------------------------

print(f"a={a}\nb={b}\nc={c}")
print(f"a={a}\tb={b}\tc={c}")

# -----------------------------------------
# Old-style formatting
# -----------------------------------------

a = 10
b = 23.4
c = "string"

print("a=%d\nb=%f\nc=%s" % (a, b, c))
print("a=%d\nb=%.2f\nc=%s" % (a, b, c))

# -----------------------------------------
# .format method
# -----------------------------------------

print("a={}\tb={}\tc={}".format(a, b, c))
print("a={2}\tb={1}\tc={0}".format(a, b, c))
