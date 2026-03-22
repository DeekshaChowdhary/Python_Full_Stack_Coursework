# ------------------ PYTHON DICTIONARY ------------------------

# 🔹 1. Creating Dictionary
d = {}              # empty dictionary
d = dict()          # another way
s = set()           # empty set (difference)

# 🔹 2. Example Dictionary
data = {
    'name': 'a',
    'age': 25,
    'course': 'PFS',
    'skills': ['python', 'java', 'c++']
}

# 🔹 3. Adding Elements (keys must be immutable)
d[1.1] = 'float'
d['dfgh'] = 'string'
d[True] = 'bool'
d[2+3j] = 'complex'
d[(1,2,3)] = 'tuple'   # allowed (tuple is immutable)

# 🔹 4. Accessing Values
print(data['name'])
print(data['age'])

# 🔹 5. Dictionary Methods
print(data.items())    # key-value pairs
print(data.keys())     # only keys
print(data.values())   # only values

# 🔹 6. Other Operations
print(len(data))       # number of items
print(id(data))        # memory address

print(sorted(data))    # sorted keys
print(max(data))       # max key
print(min(data))       # min key

# 🔹 7. Updating Dictionary
data['k1'] = 'v1'      # add single key-value

data.update({
    'k2': 'v2',
    'k3': 'v3'
})                     # add multiple

# 🔹 8. Deleting Elements
del data['k1']         # delete by key

data.pop('name')       # remove key and return value
data.pop('age')

# 🔹 9. Clear Dictionary
data.clear()           # removes all items

# 🔹 10. Important Points
# - Dictionary is mutable
# - Keys must be unique
# - Keys must be immutable (int, str, tuple)
# - Values can be any datatype
# ✔ No indexing → access using keys
