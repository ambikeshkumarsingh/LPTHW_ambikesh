def add(a,b):
    print(f"ADDING {a}+{b}")
    return a+b

def subtract(a,b):
    print(f"SUBTRACTNG {a}-{b}")
    return a-b

def multiply(a,b):
    print(f"MULTIPLYING {a}*{b}")
    return a*b

def division(a,b):
    print(f"DIVIDING {a}/{b}")
    return a/b

print("let's do some maths \n")
age =add(30,5)
height=subtract(78,4)
weight=multiply(90,2)
iq=division(100,2)

print(f"Age is {age} , Height is {height}, Weight is {weight} ,  IQ is {iq}")
