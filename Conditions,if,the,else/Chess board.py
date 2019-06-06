x1 = int(input())
x2 = int(input())
y1 = int(input())
y2 = int(input())
if((x1+x2)%2==0 and (y1+y2)%2==1):
    print("NO")
elif((y1+y2)%2==0 and (x1+x2)%2==1):
    print("NO")
else:
    print("YES")