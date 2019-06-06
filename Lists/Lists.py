# LISTS
# 1.Even indices
a = input().split()
for i in range(0, len(a), 2):
    print(a[i])

# 2.Even Elements
a = [int(i) for i in input().split()]
for elem in a:
    if elem % 2 == 0:
        print(elem)

# 3.Greater than previous
a = [int(i) for i in input().split()]
for i in range(1, len(a)):
    if a[i] > a[i-1]:
        print(a[i])

# 4. Neighbors of the same sign
a = [int(i) for i in input().split()]
for i in range(1, len(a)):
    if(a[i-1]*a[i] > 0):
        print(a[i-1], a[i])
        break

# 5. Greater than neighbours
count = 0
a = [int(i) for i in input().split()]
for i in range(1, len(a)-1):
    if(a[i] > a[i-1] and a[i] > a[i+1]):
        count += 1
print(count)

# 6. The largest element
max = -999999999999
a = [int(i) for i in input().split()]
for i in range(0, len(a)):
    if(a[i] > max):
        max = a[i]
        indexmax = i
print(max, indexmax)

# 7. The number of distinct elements
a = [int(i) for i in input().split()]
count = 1
for i in range(0, len(a)-1):
    if(a[i] != a[i+1]):
        count += 1
print(count)

# 8. Swap neighbours
a = [int(i) for i in input().split()]
for i in range(0, len(a)-1, 2):
    sum = a[i] + a[i+1]
    a[i] = sum - a[i]
    a[i+1] = sum - a[i+1]
for i in a:
    print(i)

# 9. Swap min and max

indexmax = 0
indexmin = 0
a = [int(i) for i in input().split()]
for i in range(1, len(a)):
    if(a[i] > a[indexmax]):
        indexmax = i
    elif(a[i] < a[indexmin]):
        indexmin = i
a[indexmax], a[indexmin] = a[indexmin], a[indexmax]
for i in a:
    print(i)

# 10. The number of pairs of equal
a = [int(i) for i in input().split()]
count = 0
for i in range(0, len(a)-1):
    for j in range(i+1, len(a)):
        if a[i] == a[j]:
            count += 1
print(count)

# 11. Unique elements
a = [int(i) for i in input().split()]
count = list()
for i in range(0, len(a)):
    if a.count(a[i]) == 1:
        count.append(a[i])
for i in count:
    print(i)

# 12. Queens
b = []
for i in range(0, 8):
    a = [int(i) for i in input().split()]
    b.append(a)
correct = True
for i in range(0, len(b)-1):
    for j in range(i+1, len(b)):
        if abs(b[i][0]-b[j][0]) == abs(b[i][1]-b[j][1]) or (b[i][0] == b[j][0] or b[i][1] == b[j][1]):
            correct = False
if correct:
    print("NO")
else:
    print("YES")

# 13.The bowling alley
