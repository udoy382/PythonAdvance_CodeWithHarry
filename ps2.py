# Python - Practice Set 


# Q1

# make 2 virtual environment and install some packages on both ~

# ==> pip install virtualenv
# ==> virtualenv env 
# ==> pip install (pkg name)
# ==> pip freeze 
# ==> pip freeze > requirements.txt 
# ==> pip install -r requirements.txt

# Q2
"""
name = input("Enter Your Name > ")
marks = int(input("Enter Your Marks > "))
phone_number = input("Enter Your Phone Number > ")


info = "The name of the student is {}, his marks is {} and his phone number is {}".format(name, marks, phone_number)
print(info)
"""

# Q3
"""
user = int(input("Enter the number > "))

l = [str(i * user) for i in range(1, 11)]
print(l)

verticalTable = "\n".join(l)
print(verticalTable)
"""

# Q4
"""
l = [1, 2, 3, 4, 5, 6, 4, 3, 6, 76, 75, 45, 34, 65, 34, 65, 34,54,65,3,23,5,6,7,54]

a = filter(lambda a: a % 5 == 0, l)
print(list(a))
"""

# Q5
"""
from functools import reduce

l = [3, 4, 7, 9, 7, 11]

a = reduce(max, l)
print(a)
"""

# Q6
"""
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>This site is for practice</h1>"

if __name__ == "__main__":
    app.run(debug=True)
"""