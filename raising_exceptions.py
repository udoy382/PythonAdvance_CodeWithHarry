def increment(num):
    try:
        return int(num) + 1
    except:
        raise ValueError("This is not good - This is a custom message")
    
a = increment(34)

print(a)