a = [3, 6, 6, 7, 6, 455, 3, 44, 34, 23, 56, 45, 34, 5, 4, 343, 34, 56, 4, 3, 55, 10]

"""
b = []

for item in a:
    if item % 2 == 0:
        b.append(item)

print(b)
"""

# Shortcut to write the same:
b = [i for i in a if i % 2 == 0]
print(b)


t = [1, 4, 2, 4, 1, 2, 3]
s = {i for i in t}
print(s)