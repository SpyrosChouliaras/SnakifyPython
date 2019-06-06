x1 = int(input())
x2 = int(input())
y1 = int(input())
y2 = int(input())
if((y1==x1 or y1 ==x1+1 or y1==x1-1) and (y2==x2 or y2==x2+1 or y2==x2-1)):
    print("YES")
else:
    print("NO")