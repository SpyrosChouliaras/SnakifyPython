# STRINGS
# 1. Slices
string = input()
print(string[2])
print(string[-2])
print(string[0:5])
print(string[:-2])
print(string[:: 2])
print(string[1::2])
print(string[::-1])
print(string[::-2])
print(len(string))

# 2.The number of words
string = input().split()
print(len(string))

# 3.The first and last occurence
string = input()
if string.count("f") == 1:
    print(string.find("f"))
elif string.count("f") >= 2:
    print(string.find("f"), string.rfind("f"))

# (4.)The second occurrence
string = input()
if string.count('f') == 1:
    print(-1)
elif string.count('f') < 1:
    print(-2)
else:
    print(string.find('f', string.find('f') + 1))

# (5.)Remove the fragment
string = input()
if string.count("h") >= 2:
    print(string[0:string.find("h")] + string[string.rfind("h")+1:len(string)])

# 4.Reverse the fragment
string = input()
if string.count("h") >= 2:
    reversepart = string[string.find("h"):string.rfind("h")+1]
    print(string[0:string.find("h")] + reversepart[::-1] + string[string.rfind("h")+1:len(string)])


# 5.Replace within the fragment
string = input()
if string.count("h") >= 2:
    fragment = string[string.find("h")+1:string.rfind("h")]
    print(string[0:string.find("h")+1]+fragment.replace("h", "H") +
          string[string.rfind("h"):len(string)])

# 6. Delete every third character
string = input()
result = ""
for i in range(0, len(string)):
    if i % 3 != 0:
        result += string[i]
print(result)
