number = int(input())
a = number%10
b = (number/10) % 10
b = int(b)
c = (number/100)%10
c = int(c)
result = a + b + c
print(result)