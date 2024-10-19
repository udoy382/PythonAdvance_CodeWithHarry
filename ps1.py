# Question-1
"""
def readFile(filename):
    try:
        with open(filename, "r") as f:
            print(f.read())
    except FileNotFoundError:
        print(f"File {filename} is not found")


readFile("1.txt")
readFile("2.txt")
readFile("3.txt")
readFile("4.txt")
"""

# Question-2
"""
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for index, item in enumerate(l):
    if index == 2 or index == 4 or index == 6:
        # print(index, item)
        print(f"The {index + 1} element is {item}")
"""

# Question-3
"""
num = int(input("Enter your number > "))
table = [num * i for i in range(1, 11)]
print(table)
"""


# Question-4
"""
a = int(input("Enter number a > "))
b = int(input("Enter number b > "))

try:
    print(a // b)
except:
    print("Infinite")
"""


# Question-5

num = int(input("Enter your number > "))
table = [num * i for i in range(1, 11)]
print(table)

with open("tables.txt", "a") as f:
    f.write(str(table))
    f.write("\n")