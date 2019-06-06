#List of squares
N = int(input())
i=1
while i**2 <=N:
    print(i**2)
    i +=1

#Least divison

n = int(input())
i = 2
while n%i !=0:
    i += 1
print(i)

#The power of two

N = int(input())
i = 1
count = 0
while(i*2 <= N):
    i = i*2
    count += 1
print(count, i)

#Morning jog

x = int(input())
y = int(input())
count = 1
while x < y:
    x += 0.10*x
    count += 1
print(count)

#The length of the sequence

x = int(input())
count = 0
while x != 0:
    x = int(input())
    count += 1
print(count)

#The sum of the sequence

x = int(input())
sum = 0
while x != 0:
    sum += x
    x = int(input())
print(sum)

#The average of the sequence

sum = 0
count = 0
x = int(input())
while x !=0:
    sum += x
    count +=1
    x = int(input())
print(sum/count)

#The maximum of the sequence

max = int(input())
y = 1
while y != 0:
    y = int(input())
    if (y > max):
        max = y
print(max)

#The index of the maximum of a sequence

max = 0
index_of_max = -1
element = -1
len = 1
while element != 0:
    element = int(input())
    if element > max:
        max = element
        index_of_max = len
    len += 1
print(index_of_max)

#The number of even elements of the sequence

x = 1
count = 0
while x != 0:
    x = int(input())
    if(x % 2 == 0 and x != 0):
        count += 1
print(count)


#The number of elements that are greater than the previous one

x = int(input())
max = x
count = 0
while x != 0:
    x = int(input())
    if(x > max):
        count += 1
    max = x
print(count)

#The second maximum

a = int(input())
firstmax = -999999
secondmax = -999999

while(a!=0):

    if a>firstmax:
        secondmax=firstmax
        firstmax = a
    else:
        if a > secondmax:
            secondmax = a
    a = int(input())
print(secondmax)

#The number of elements equal to the maximum
x = int(input())
max = x
count = 1
while x != 0:
    x = int(input())
    if(x == max and x != 0):
        count += 1
    if(x > max and x != 0):
        max = x
        count = 1
print(count)

#Fibonacci numbers

n = int(input())
if n == 0:
    print(0)
elif n == 1:
    print(1)
else:
    x1 = 0
    x2 = 1
    for i in range(1, n):
        sum = x1 + x2
        x1 = x2
        x2 = sum
    print(sum)

#The index of a fibonacci numbers

a = int(input())
if a == 0:
    print(0)
else:
    fib_prev, fib_next = 0, 1
    n = 1
    while fib_next <= a:
        if fib_next == a:
            print(n)
            break
        fib_prev, fib_next = fib_next, fib_prev + fib_next
        n += 1
    else:
        print(-1)

#The maximum number of consecutive equal elements

prev = -10
reps = 0
maxreps = 0
element = int(input())
while element != 0:
    if prev == element:
        reps += 1
    else:
        prev = element
        maxreps = max(maxreps, reps)
        reps = 1
    element = int(input())
maxreps = max(maxreps, reps)
print(maxreps)
