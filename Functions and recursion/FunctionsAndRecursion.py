#The length of the segment

import math
x = float(input())
y = float(input())
z = float(input())
k = float(input())


def distance(x1, y1, x2, y2):
    sq1 = (x1-x2)**2
    sq2 = (y1-y2)**2
    return math.sqrt(sq1 + sq2)


print(distance(x, y, z, k))

#Negative exponent

a = float(input())
n = int(input())


def power(a, n):
    pow = a**n
    return pow


print(power(a, n))

#Uppercase

a = str(input())
print(a.title())

#Exponentiation

def math_pow(a, n):
    if a == 0:
        return 0
    elif a != 0 and n == 0:
        return 1
    elif a != 0 and n == 1:
        return a
    else:
        return a * math_pow(a, n-1)


x = float(input())
y = float(input())
print(math_pow(x, y))

#Reverse the sequence

def reverse():
    x = int(input())
    if x != 0:
        reverse()
    print(x)

reverse()

#Fibonacci numbers
a = int(input())
def fibonacci(n):
    a = 0
    b = 1
    c = 0
    for i in range(n-1):
        c = a+b
        a = b
        b = c
    return(b)

print(fibonacci(a))
