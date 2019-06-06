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
