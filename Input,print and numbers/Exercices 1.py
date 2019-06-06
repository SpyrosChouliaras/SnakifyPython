#1.  Sum of three numbers
a = int(input())
b = int(input())
c = int(input())
print(a + b + c)

#2.  Area of right-angled triangle
b = int(input())
h = int(input())
result = (b*h)/2
print(result)

#3.  Apple sharing
n= int(input())
k = int(input())

print(int(k/n))
print(k%n)

# 4.  Hello, Harry!
name = input()

print("Hello, {}!".format(name))

#5.  Previous and next
a = int(input())
next = a+1
previous = a-1

print("The next number for the number %d is %d" %(a,next))
print("The previous number for the number %d is %d"%(a,previous))

#6.  School desks 
a = int(input())
b = int(input())
c = int(input())

if(a%2==0):
    deska=a/2
else:
    deska=(a+1)/2
if(b%2==0):
    deskb=b/2
else:
    deskb=(b+1)/2
if(c%2==0):
    deskc=c/2
else:
    deskc=(c+1)/2
result = deska + deskb + deskc
result = int(result)
print(result)

# 7.Last digit of integer
a = int(input())

lastdigit = a % 10

print(lastdigit)

# 8. Tenth digit
number = int(input())
x = (number/10) % 10
x = int(x)
print(x)

# 9. Sum of digits
number = int(input())
a = number % 10
b = (number/10) % 10
b = int(b)
c = (number/100) % 10
c = int(c)
result = a + b + c
print(result)

# 10. Fractional part
number = float(input())
number = number - int(number)
print(number)

# 11. First digit after decimal point
number = float(input())
number = number - int(number)
number = int(number*10)
print(number)

# 12. Car route
N = int(input("give"))
M = int(input("give"))
y = N
count = 1
while(y//M == 0):
    y = y+N
    count += 1

print(count)

# 13. Digital Clock
N = int(input())
hours = N//60
minutes = N % 60
print(hours, minutes)

# 14. Total Cost
a = int(input())
b = int(input())
n = int(input())
cost = n * (100 * a + b)
print(cost // 100, cost % 100)

# 15. Clock Face-1
H = int(input())
M = int(input())
S = int(input())
degrees = H*30 + M*0.5 + S*(30/3600)
print(degrees)

# 17.  Minimum of two numbers
x = int(input())
y = int(input())
if(x < y):
    print(x)
else:
    print(y)

# 18.  Sign function
X = int(input())
if(X > 0):
    print(1)
elif(X < 0):
    print(-1)
else:
    print(0)

# 19. Minimum of three numbers
x = int(input())
y = int(input())
z = int(input())
if(x < y):
    if(x < z):
        print(x)
    else:
        print(z)
elif(x < z):
    if(y < z):
        print(y)
    else:
        print(z)
else:
    if(y < z):
        print(y)
    else:
        print(z)

# 20. Leap year
year = int(input())
if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
    print("LEAP")
else:
    print("COMMON")

# 21. Equal numbers
x = int(input())
y = int(input())
z = int(input())
if(x == y and x == z and y == z):
    print(3)
elif(x == y or x == z or y == z):
    print(2)
else:
    print(0)

# 22. Rook move
x1 = int(input())
x2 = int(input())
y1 = int(input())
y2 = int(input())
if(x1 == y1 or x2 == y2):
    print("YES")
else:
    print("NO")

# 23. Chess board
x1 = int(input())
x2 = int(input())
y1 = int(input())
y2 = int(input())
if((x1+x2) % 2 == 0 and (y1+y2) % 2 == 1):
    print("NO")
elif((y1+y2) % 2 == 0 and (x1+x2) % 2 == 1):
    print("NO")
else:
    print("YES")

# 24. King move
x1 = int(input())
x2 = int(input())
y1 = int(input())
y2 = int(input())
if((y1 == x1 or y1 == x1+1 or y1 == x1-1) and (y2 == x2 or y2 == x2+1 or y2 == x2-1)):
    print("YES")
else:
    print("NO")

# 25. Bishop moves
x1 = int(input())
x2 = int(input())
y1 = int(input())
y2 = int(input())
if abs(x1-y1) == abs(x2-y2):
    print("YES")
else:
    print("NO")

# 26. Queen move
x1 = int(input())
x2 = int(input())
y1 = int(input())
y2 = int(input())
if(abs(x1-y1) == abs(x2-y2)):
    print("YES")
elif((x1 == y1 or x2 == y2)):
    print("YES")
else:
    print("NO")

# 27. Knight move
x1 = int(input())
x2 = int(input())
y1 = int(input())
y2 = int(input())
if (x1+x2) % 2 == 1:
    if (y1+y2) % 2 == 0 and 1 <= abs(x1-y1) <= 2 and 1 <= abs(x2-y2) <= 2:
        print("YES")
    else:
        print("NO")
elif((x1+x2) % 2 == 0):
    if (y1+y2) % 2 == 1 and 1 <= abs(x1-y1) <= 2 and 1 <= abs(x2-y2) <= 2:
        print("YES")
    else:
        print("NO")

# 28. Chocolate bar
n = int(input())
m = int(input())
k = int(input())
portions = n*m
if k < n*m and ((k % n == 0) or (k % m == 0)):
    print("YES")
else:
    print("NO")
