# -----------------------------------------
# Tuple Creation
# -----------------------------------------

# Empty tuples
t = ()
print("Empty tuple:", t)

t = tuple()
print("Empty tuple using tuple():", t)

# Tuple with values
t = (1, 2, 3, 4, 5, 1, 2, 4)
print("Tuple with values:", t)

# Using tuple() correctly
t = tuple((1, 2, 3, 4, 5))
print("Using tuple() constructor:", t)

# Tuple packing
t = (1, 2, 3, 4, 5)
print("Tuple packing:", t)

# Single element tuple
t = (1,)
print("Single element tuple:", t)

t = ("int", "float", "complex", "bool", "set", "dict", "list", "tuple", "string")
print("Tuple of datatypes:", t)

# -----------------------------------------
# Indexing
# -----------------------------------------

print("t[1]:", t[1])
print("t[-1]:", t[-1])
print("t[-2]:", t[-2])
print("t[-5]:", t[-5])
print("t[2]:", t[2])
print("t[3]:", t[3])

# -----------------------------------------
# Slicing
# -----------------------------------------

print("t[3:6]:", t[3:6])
print("t[-1:-4]:", t[-1:-4])
print("t[-1:-4:-1]:", t[-1:-4:-1])
print("t[-3:]:", t[-3:])
print("t[2::-1]:", t[2::-1])
print("t[::2]:", t[::2])
print("t[::-2]:", t[::-2])

# -----------------------------------------
# Tuple Operations
# -----------------------------------------

t1 = (1, 2, 3)
t2 = (7, 8, 9)

print("t1:", t1)
print("t2:", t2)

# Concatenation
print("t1 + t2:", t1 + t2)

# Repetition
print("t1 * 5:", t1 * 5)

# Membership
print("3 in t1:", 3 in t1)
print("5 in t1:", 5 in t1)
print("4 not in t1:", 4 not in t1)
print("1 not in t1:", 1 not in t1)

# -----------------------------------------
# Tuple Unpacking
# -----------------------------------------

t = (10, 20, 30)
a, b, c = t
print("Unpacked values:", a, b, c)

t = ('Uname', 'mail@gmail.com', 'Pwd@123')
uname, mail, pwd = t
print("Username:", uname)
print("Email:", mail)
print("Password:", pwd)

# -----------------------------------------
# Tuple Methods
# -----------------------------------------

t = (1, 2, 3, 1, 2, 3, 1, 2)
print("Tuple for methods:", t)

print("Count of 2:", t.count(2))
print("Count of 3:", t.count(3))
print("Count of 1:", t.count(1))

print("Index of 2:", t.index(2))

# -----------------------------------------
# Built-in Functions
# -----------------------------------------

print("Length:", len(t))
print("Max value:", max(t))
print("Min value:", min(t))
print("Sum:", sum(t))

# -----------------------------------------
# Tuple immutability
# -----------------------------------------

print("Tuples are immutable, you cannot modify items.")
print("Example: t[1] = 14 will cause an error.")