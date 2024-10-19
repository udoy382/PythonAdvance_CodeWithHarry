# map ==>
'''
def square(num):
    return num * num

l = [1, 2, 4]

# Method 1 ~
"""
l2 = []
for item in l:
    l2.append(square(item))

print(l2)
"""

# Method 2 ~

print(list(map(square, l)))
'''

# filter ==>
"""
def greater_than_5(num):
    if num > 5:
        return True
    else:
        return False
    
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 20, 30]

print(list(filter(greater_than_5, l)))
"""

# reduce ==>

from functools import reduce

l = [1, 2, 3, 4, 5, 6, 7]

sum = lambda a, b: a + b

val = reduce(sum, l)
print(val)