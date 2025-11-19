# Basic input examples
name = input("Enter the name: ")
print(name)

age = int(input("Enter the age: "))
print(age)

discount = float(input("Enter the discount: "))
print(discount)

# Input of multiple strings
names = input("Enter multiple names: ")
print(names)

names = input("Enter multiple names: ").split()
print(names)

# map() with int
nums = list(map(int, input("Enter integer values: ").split()))
print(nums)

# map() with float
nums_float = list(map(float, input("Enter float values: ").split()))
print(nums_float)

# tuple input
t1 = tuple(input("Enter words for tuple: ").split())
print(t1)

t2 = tuple(map(int, input("Enter integers for tuple: ").split()))
print(t2)

t3 = tuple(map(float, input("Enter floats for tuple: ").split()))
print(t3)

# set input
s1 = set(map(int, input("Enter values for set: ").split()))
print(s1)

s2 = set(input("Enter words for set: ").split())
print(s2)

# eval input
data = eval(input("Enter eval data: "))
print(data)

# input → splitting into two variables
a, b = input("Enter username and email: ").split()
print(a, b)

# input with map → two integers
x, y = list(map(int, input("Enter 2 integers: ").split()))
print(x, y)

# multiple variable assignment
p, q, r = 10, 20, 30
print(p, q, r)

# print examples
print("a=", p, "b=", q, "c=", r)
print("a=", p, "\nb=", q, "\nc=", r)
print("a=", p, "\tb=", q, "\tc=", r)

# sep and end examples
print("a=", p, "\tb=", q, "\tc=", r, sep='')
print("a=", p, "\tb=", q, "\tc=", r, sep='\t\t')
print("a=", p, "b=", q, "c=", r, end='\n\n')

# f-string examples
print(f'a={p}\nb={q}\nc={r}')
print(f'a={p}\tb={q}\tc={r}')

# % formatting
a = 10
b = 23.4
c = "string"
print('a=%d\nb=%f\nc=%s' % (a, b, c))
print('a=%d\nb=%.2f\nc=%s' % (a, b, c))

# format() method
print('a={}\tb={}\tc={}'.format(a, b, c))
print('a={2}\tb={1}\tc={0}'.format(a, b, c))
