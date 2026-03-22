# ---------------------- PYTHON SET ------------------------------

"""
 Key Points:
- Set is unordered (no indexing)
- Set does not allow duplicates
- Set is mutable (can add/remove items)
- Elements must be immutable (int, str, tuple, etc.)
"""


# 🔹 1. Creating Sets
s = {}          # This creates a dictionary, not a set
s = set()       # Empty set

s = {5678, 546, 23, 454, 124, 1324}
print(s)


# 🔹 2. Adding Elements
s.add(124)      # duplicate → no change
s.add(12.3)
s.add('String')
s.add(2+3j)
s.add(False)

print(s)


# 🔹 3. Invalid Additions (Unhashable Types)
# s.add({1,2,3})      set
# s.add([1,2,3])      list
# s.add({1:2})        dictionary


# 🔹 4. Removing Elements
s.remove(124)   # error if not found
s.discard(3)    # no error if not found
s.pop()         # removes random element

print(s)


# 🔹 5. Updating Set
s.add(1)
s.update({2, 3, 4})   # add multiple elements

print(s)


# 🔹 6. Looping
for i in s:
    print(i)


# 🔹 7. Set Operations
a = {9, 7, 8, 3, 1}
b = {2, 3, 4, 5}

print(a & b)   # intersection (common elements)
print(a | b)   # union (all elements)
print(a - b)   # difference


# 🔹 8. Subset & Superset
print({9}.issubset(a))       # True if subset
print({9}.issuperset(a))     # False
print(a.isdisjoint(b))       # True if no common elements
print({0}.isdisjoint(a))     # True


# 🔹 9. Built-in Methods
print(a.union(b))
print(a.intersection(b))


# 🔹 10. Other Functions
print(len(a))
print(max(a))
print(min(a))
print(sorted(a))   # returns list


# 🔹 11. Clearing Set
a.clear()
print(a)


# 🔹 12. Invalid Operations (Not Allowed)
# s[0]         no indexing
# s[1:2]       no slicing
# s * 2        no repetition
