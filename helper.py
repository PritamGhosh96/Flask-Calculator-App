import math
def add(a: int, b: int) -> str:
    return "Addition of {} and {} is {}".format(a,b,a+b)

def substract(a: int, b: int) -> str:
    return "Substraction of {} from {} is {}".format(b,a,a-b)

def multiply(a: int, b: int) -> str:
    return "Multiplication of {} with {} is {}".format(a,b,a*b)

def division(a: int, b: int) -> str:
    if b == 0:
        return "Can not divide by Zero!"
    return "Division of {} by {} is {}".format(a,b,a/b)

def log(a: int, b: int) -> str:
    if b == 0:
        return "Can not have log with base Zero!"
    if a <= 0:
        return "Can not have logirthm with a number less than or equals to Zero!"
    return "Logarithm base {} of {} is {}".format(b,a,math.log(a,b))