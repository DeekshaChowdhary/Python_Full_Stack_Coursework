###----BASIC LIST COMMANDS----------------###
# 🔹 1. Creating list
a = [10, 20, 30]
b = ["apple", "banana", "cherry"]
c = [1, "hello", 3.5]   # mixed list


# 🔹 2. Accessing elements
print(a[0])     # 10
print(a[-1])    # last element


# 🔹 3. Slicing
print(a[0:2])   # [10, 20]
print(a[:])     # full list


# 🔹 4. Adding elements
a.append(40)        # add at end
a.insert(1, 15)     # insert at index


# 🔹 5. Removing elements
a.remove(20)    # remove by value
a.pop()         # remove last
a.pop(1)        # remove by index


# 🔹 6. Updating elements
a[0] = 100


# 🔹 7. Length of list
print(len(a))


# 🔹 8. Sorting
a.sort()                 # ascending
a.sort(reverse=True)     # descending


# 🔹 9. Reverse list
a.reverse()


# 🔹 10. Searching
print(10 in a)       # True/False
print(a.index(30))   # index of element


# 🔹 11. Counting
print(a.count(10))


# 🔹 12. Copy list
b = a.copy()


# 🔹 13. Clearing list
a.clear()


# 🔹 14. Loop through list
for i in b:
    print(i)


# 🔹 15. Extend list
b.extend([50, 60])


# 🔹 16. Concatenation
c = b + [70, 80]


# 🔹 17. Repetition
d = [1, 2] * 3   # [1, 2, 1, 2, 1, 2]


# 🔹 18. Nested list
products = [["laptop", 56000], ["phone", 76000]]
print(products[0][0])   # laptop


# 🔹 19. Delete list or element
del b[0]
# del b   # deletes full list


# 🔹 20. Min & Max
nums = [5, 2, 9]
print(min(nums))
print(max(nums))
