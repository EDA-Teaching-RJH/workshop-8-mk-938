def add(a,b):
    return (a + b)

def sub(a,b):
    return (a - b)

def div(a,b):
    if b == 0:
        raise ZeroDivisionError #ValueError
    return (a / b)

def mult(a,b):
    return (a * b)

