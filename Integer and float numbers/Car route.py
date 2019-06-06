N = int(input("give"))
M = int(input("give"))
y=N
count=1
while(y//M == 0):
    y = y+N
    count+=1

print (count)



