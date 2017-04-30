def factorial(x: int):
    result = 1
    for i in range(1, x+1):
        result *= i
    return result

print(factorial(100)/3600/24/365/1000/1000/1000)