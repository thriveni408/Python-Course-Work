# List creation and basic operations
l = []
l = list()
l = [1, 2, 3, 4, 5, 6]
l = list([1, 2, 3, 4, 5])

# Nested lists
l = [[1, 2], [3, 4], [5, 6]]

# List repetition
l = [1, 1, 1, 1, 1, 1, 2]
print(l)
print([1, 2, 3] + [4, 5, 6])
print([1, 2] * 5)

# Membership
print(2 in l)
print(6 in l)

# String lists and slicing
l = ['ajay', 'krishna', 'shekar', 'santhosh', 'harsha', 'varun', 'shiva']
print(l[2], l[-3], l[-2], l[-1], l[1], l[0])
print(l[1:3])
print(l[-1:-4:-1])
print(l[::2])
print(l[1::2])
print(l[::-1])

# Accessing nested lists
l = [[1, 2], [3, 4], [5, 6]]
print(l[2], l[1], l[0])
print(l[0][0], l[2][0], l[1][1])

# Modifying list elements
l = [10, 20, 30, 40, 50]
print(id(l))
l[1] = 20.3
l[2] = 30 + 4j
l[3] = 'string'
print(l)

# Appending, extending, and inserting elements
l.append([1, 2, 3])
l.append((10, 202, 30))
l.append(70)
l.append(80)
l.extend([100, 90, 20, 10])
l.insert(0, 10)
l.insert(5, {1: 2, 2: 4, 3: 6, 4: 8})
l.insert(8, {1, 2, 3, 4})
print(l)

# Removing elements
l.remove(10)
l.remove((10, 202, 30))
l.remove({1, 2, 3, 4})
l.remove(100)
print(l)

# Popping elements
l.pop(2)
l.pop(1)
l.pop()
print(l)

# Deleting and clearing
del l[2]
print(l)
l.clear()
print(l)

# Index, count, sort, reverse
l = [10, 20, 30, 40, 50, 60, 70, 80]
print(l.index(30))
print(l.index(80))
l.append(10)
print(l.index(10))
print(l.count(10))
l.sort()
print(l)
l.sort(reverse=True)
print(l)
l.reverse()
print(l)

# Copying lists
a = [1, 2, 3, 4, 5]
b = a
b.append(6)
print(a, b)
c = a.copy()
c.append(9)
print(a, c)

# Max, min, len
l = [1, 2, 3, 3, 4, 4, 8, 8]
print(max(l))
print(min(l))
print(len(l))

# any() and all()
l = [0, 0.0, '', [], (), {}, set(), False]
print(any(l))
print(all(l))
l.append(1)
print(any(l))
print(all(l))

a = [1, 2, 3, 4, 5, 6]
print(all(a))
