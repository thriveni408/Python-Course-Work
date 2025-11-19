# -----------------------------
# LIST CREATION
# -----------------------------
l = []
print("Empty list:", l)

l = list()
print("Empty list using list():", l)

l = [1,2,3,4,5,6]
print("List:", l)

l = list([1,2,3,4,5])
print("List using list([..]):", l)

# -----------------------------
# LIST OPERATIONS
# -----------------------------
l = [1,1,1,1,1,1,2]
print("List with duplicates:", l)

print("Concatenation:", [1,2,3] + [4,5,6])
print("Repetition:", [1,2] * 5)

print("2 in l:", 2 in l)
print("6 in l:", 6 in l)

# -----------------------------
# INDEXING & SLICING
# -----------------------------
l = ['ajay','krishna','shekar','santhosh','harsha','varun','shiva']
print("List:", l)

print("l[2]:", l[2])
print("l[-3]:", l[-3])
print("l[-2]:", l[-2])
print("l[-1]:", l[-1])
print("l[1:3]:", l[1:3])
print("l[-1:-4:-1]:", l[-1:-4:-1])
print("l[::2]:", l[::2])
print("l[1::2]:", l[1::2])
print("l[::-1]:", l[::-1])

# -----------------------------
# NESTED LISTS
# -----------------------------
l = [[1,2],[3,4],[5,6]]
print("Nested list:", l)
print("l[2]:", l[2])
print("l[0][0]:", l[0][0])
print("l[2][0]:", l[2][0])
print("l[1][1]:", l[1][1])

# -----------------------------
# MUTABILITY
# -----------------------------
l = [10,20,30,40,50]
print("Original list:", l)

l[1] = 20.3
print("After changing index 1:", l)

l[2] = 30 + 4j
print("After adding complex number:", l)

l[3] = "string"
print("After adding string:", l)

# -----------------------------
# APPEND / EXTEND / INSERT
# -----------------------------
l.append([1,2,3])
print("After append list:", l)

l.append((10,202,30))
print("After append tuple:", l)

l.append(70)
l.append(80)
print("After appending 70,80:", l)

l.extend([100,90,20,10])
print("After extend:", l)

l.insert(0,10)
print("After inserting 10 at 0:", l)

l.insert(5, {1:2,2:4,3:6,4:8})
print("After inserting dict:", l)

l.insert(8, {1,2,3,4})
print("After inserting set:", l)

# -----------------------------
# REMOVE / POP
# -----------------------------
print("Before remove:", l)
l.remove(10)
print("After remove first 10:", l)

l.remove((10,202,30))
print("After removing tuple:", l)

l.remove({1,2,3,4})
print("After removing set:", l)

l.remove(100)
print("After removing 100:", l)

# POP
print("l.pop(2):", l.pop(2))
print("After pop(2):", l)

print("l.pop():", l.pop())
print("After last pop:", l)

# -----------------------------
# DEL / CLEAR
# -----------------------------
l = [10,50,[1,2,3],70]
del l[2]
print("After del l[2]:", l)

l.clear()
print("After clear:", l)

# -----------------------------
# INDEX / COUNT
# -----------------------------
l = [10,20,30,40,50,60,70,80]
print("Index of 30:", l.index(30))

l.append(10)
print("List:", l)

print("Index of 10:", l.index(10))
print("Count of 10:", l.count(10))

# -----------------------------
# SORT / REVERSE
# -----------------------------
l = [8,2,3,4,1,8,3,4]
print("Original:", l)

print("sorted(l):", sorted(l))

l.sort()
print("After sort:", l)

l.sort(reverse=True)
print("Sort reverse:", l)

l.reverse()
print("After reverse:", l)

# -----------------------------
# ASSIGNMENT vs COPY
# -----------------------------
a = [1,2,3,4,5]
b = a
b.append(6)

print("a after b.append:", a)
print("b:", b)

c = a.copy()
c.append(9)

print("c:", c)
print("a:", a)

# -----------------------------
# MAX / MIN / LEN
# -----------------------------
l = [1,2,3,3,4,4,8,8]
print("max:", max(l))
print("min:", min(l))
print("len:", len(l))

# -----------------------------
# ANY / ALL
# -----------------------------
l = [0,0.0,'',[],(),{},set(),False]
print("any(l):", any(l))
print("all(l):", all(l))

l.append(1)
print("After append 1:", l)
print("any(l):", any(l))

a = [1,2,3,4,5,6]
print("all(a):", all(a))