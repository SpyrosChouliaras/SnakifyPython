#For loop with range
#Series -1
A = int(input())
B = int(input())
if(A<=B):
    for i in range(A,B+1):
        print(i)

#Series -2
A = int(input())
B = int(input())
if (A<B):
    for i in range(A,B+1):
        print(i,end=' ')
else:
    for j in range(A,B-1,-1):
        print(j,end=' ')

#Sum of ten numbers
sum=0
for i in range(0,10):
    x = int(input())
    sum +=x
print(sum)

#Sum of N numbers
sum = 0
N = int(input())
for i in range(0,N):
    x = int(input())
    sum += x
print(sum)

#Sum of cubes
sum = 0
N = int(input())
for i in range(1,N+1):
    sum += i**3
print(sum)

#Factorial
mult = 1
n = int(input())
for i in range(1,n+1):
    mult = mult*i
print(mult)

#The number of zeros

count=0
N = int(input())
for i in range(0,N):
    x = int(input())
    if(x==0):
        count += 1
print(count

#Adding factorials

mult = 1
sum =0
n = int(input())
for i in range(1,n+1):
    mult = mult*i
    sum += mult
print(sum)

#Ladder (Chaos is a ladder)

n = int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j, end='')
    print()

#Lost card

sum1=0
sum2=0
N = int(input())
missing = N
for i in range(0,N-1):
    x = int(input())
    sum1 += x
for j in range(1,N+1):
    sum2 += j
print(sum2-sum1)
