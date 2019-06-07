#Mock Paper - PRACTICAL 1
#Question 1
#a)
#
# def fibonacci(n):
#
#     a = 0
#     b = 1
#     sum = 0
#     for i in range(0,n):
#         print(a,end=' ')
#
#         sum = a + b
#         a = b
#         b = sum
#
# fibonacci(10)

#b)

# def fibonacci_series():
#
#     a = 0
#     b = 1
#     sum = 0
#     counter = 0
#     while(a<2000):
#
#         counter +=1
#         sum = a + b
#         a = b
#         b = sum
#
#     print(counter)
#
# fibonacci_series()


#Question 2


# def search(str,lst,size):
#
#     for i in range(0,size):
#         if lst[i] == str:
#             return i
#             break
#
#     return -1
#
# print(search("diakosmos",["something","awesome","may","diakosmos"],4))

#Question 3

# import random
#
# randomnumber = random.randint(0,99)
# counter = 1
# guess = int(input("Why dont you make a guess?"))
# while(guess != randomnumber):
#
#     counter +=1
#     if guess < randomnumber:
#         guess = int(input("Too low. Guess again : "))
#     elif guess > randomnumber:
#         guess = int(input("Too high. Guess again : "))
#
# print("Correct! It took you %d guesses"%counter)

#Question 4

# input = input("Give the answers please : ").split()
# file = open("/Users/spyroschouliaras/Desktop/exams.txt","r")
# line = file.readline().split()
# score = 0
# while (line[0] != "999"):
#
#     for i in range(0,len(input)):
#         if line[i+1] == input[i]:
#             score +=1
#         elif line[i+1] != input[i]:
#             score -=1
#         elif line[i+1] == "x":
#             continue
#
#     print(line[0] + " " + str(score) + " marks")
#     line = file.readline().split()
#     score = 0

#
#MOCK PRACTICAL 2

#Question 1

# def search(str,lst,size):
#
#     for i in range(0,size):
#         if lst[i] == str:
#             return i
#             break
#     return -1
#
# print(search("diakosmos",["ena","kaiduo","kaitria","blah"],4))
#

#Question 2

# import random
#
# number = random.randrange(0,100)
#
# guess = int(input("Why dont you make a guess ? "))
#
# counter = 1
#
# while(guess != number):
#
#     counter +=1
#
#     if guess < number:
#         guess = int(input("Too low. Guess again : "))
#     elif guess > number:
#         guess = int(input("Too high. Guess again : "))
#
# print("Correct. It took you %d guesses."%counter)
#

#Question 3

# def sqrProd(x,y):
#
#     return (x*y)*(x*y)
#
# print(sqrProd(10,10))

#Question 4

# def computeregular(list):
#     list = list.split()
#
#     if int(list[4]) > 50:
#         cost = 10 + (int(list[4])-50)*0.20
#
#     return cost
#
# def computepremium(list):
#
#     cost = 25
#     list = list.split()
#     daytime = int(list[4])
#     peaktime = int(list[5])
#     if daytime > 75:
#         cost += (daytime-75)*0.10
#     if peaktime > 100:
#         cost +=(peaktime-100)*0.5
#
#     return cost
#
#
# file = open("/Users/spyroschouliaras/Desktop/bills.txt","r")
# line = file.readline()
#
#
# while (line.split()[0] != "X0000"):
#
#
#     if line.split()[3] == "R":
#         cost = computeregular(line)
#     elif line.split()[3] == "P":
#         cost = computepremium(line)
#
#     balance = float(line.split()[2]) - cost
#
#     print(line.split()[0] + " " + line.split()[1] + " " + line.split()[3] + " " + str(cost) + " " + str(balance))
#     cost = 0
#     line = file.readline()

#MOCK PRACTICAL 3

#Question 1

# def isinside(list,number):
#
#     if number in list:
#         return True
#     else:
#         return False
#
# print(isinside([1,2,3,4,5],6))

#Question 2
#
# number = int(input("Give me a number : "))
#
# def prime(number):
#     for i in range(2,number):
#         if number%i == 0:
#           result = "The number is not a prime"
#           break
#         else:
#             result = "The number is PRIME"
#     return result
#
# print(prime(number))

#Question 3

# name = input("Please give me your String : ")
#
# def reverse(string):
#
#     string = string.split()
#     for i in range(1,len(string)+1):
#         print(string[-i],end= ' ')
#
# reverse(name)

#Question 4

# fibnumber = int(input("Give me fibonacci numbers ! "))
#
# def fibonacci(n):
#
#     a = 1
#     b = 1
#     sum = 0
#     for i in range(n):
#         print(a,end = " ")
#         sum = a+b
#         a=b
#         b=sum
# fibonacci(fibnumber)

#Question 5
#
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#
# common = [x for x in a if x in b]
# common = list(set(common))
# print(common)

#Question 6

# import random
#
# number = list(str(random.randrange(1000,9999)))
#
# guess = input("Why dont you try to guess the number ? ")
# counter = 1
# while(guess != number):
#
#     counter += 1
#
#     cows = 0
#     bulls = 0
#     cowlist = []
#     for i in range(0,len(guess)):
#         if guess[i] == number[i]:
#             cows +=1
#
#         elif guess[i] in number:
#             bulls+=1
#
#     print(number)
#     print("%d cows , %d bulls"%(cows,bulls))
#     guess = input("Why dont you try to guess the number ? ")
#

#MOCK PRACTICAL 4

#Question 1

# def swap(list):
#
#     maximum = list[0]
#     minimum= list[0]
#     minindex = 0
#     maxindex = 0
#     for i in range(0,len(list)):
#         if list[i] > maximum:
#             maximum = list[i]
#             maxindex = i
#         if list[i] < minimum:
#             minimum = list[i]
#             minindex = i
#
#     list[maxindex] = minimum
#     list[minindex] = maximum
#
#     return list
#
# print(swap([1,2,9,4,5]))

#Question 2
#a)
# def pow(a,n):
#
#     if n == 1:
#         return a
#     else:
#         return a*pow(a,n-1)
#
# print(pow(2,10))
# # b)
#
# def test():
#     assert pow(2,4)==16
#     assert pow(2,10) == 1024
#     assert pow(9,2) == 81
#     assert pow(10,2)==100

#Question 3

#
# n = 5
# allwords = []
# dict = {}
# string = """something is going to be difficult
# as we need to write something
# and we dont know how
# to write it
# blah blah blah"""
# list = []
# listsorted = []
# for word in string.split():
#     dict[word] = dict.get(word,0) + 1
#
# for i,j in zip(dict.keys(),sorted(dict.values())):
#      list.append([i,j])
#
#
# def sortSecond(val):
#     return val[1]
#
# list = sorted(list,key=sortSecond,reverse=True)
#
# print(list)
#
# for i in list:
#     print(i[0])

#Question 4
#a)
# number = int(input("Give me the number of the students : "))
# dict = {}
# allstudents = []
# atleast = []
# counter = 0
# counter2=0
# for i in range(0,number):
#     string = input()
#     for word in string.split()[1:]:
#          dict[word] = dict.get(word, 0) + 1
#
# for key,value in sorted(dict.items()):
#     if value == number:
#         allstudents.append(key)
#         counter +=1
#     if number >= 1:
#         atleast.append(key)
#         counter2+=1
#
# print(counter,allstudents)
# print(counter2,atleast)

#LAST ONE

#Question 1


#
# def number_of_above_Averages(n,m,A):
#
#     sum = 0
#     counter = 0
#     for i in range(n):
#         for j in range(m):
#             sum += A[i][j]
#
#     for i in range(n):
#         for j in range(m):
#             if A[i][j] > sum/(n*m):
#                 counter +=1
#
#     return counter
#
# def test():
#     assert number_of_above_Averages(2, 2, [[1, 1], [2, 4]]) == 1
#     assert number_of_above_Averages(2, 3, [[1, 2, 3], [4, 5, 6]]) == 3

#Question 2

# def common_elements(list1,list2):
#
#     common = [x for x in list1 if x in list2]
#     common = sorted(list(set(common)))
#
#     return common
#
# def test():
#     assert common_elements([3, 1, 2], [2, 4, 3]) == [2, 3]
#     assert common_elements([3, 3, 2], [3, 3, 4, 5]) == [3]

#Question 3

# class ManhattanTaxi:
#
#     def __init__(self,initX,initY,consumption,init_fuel):
#         self.pos = (initX,initY)
#         self.cons = consumption
#         self.fuel = init_fuel
#
#     def moveto(self,X,Y):
#
#         distance = abs(self.pos[0] - X) + abs(self.pos[1] -Y)
#         if self.fuel > distance*self.cons:
#             self.pos = (X,Y)
#             self.fuel -= distance*self.cons
#             return True
#
#         else:
#
#             return False
#
#     def add_fuel(self,fuel):
#
#         self.fuel += fuel
#
# def test():
#     t789 = ManhattanTaxi(5, 5, 1, 30)
#     assert t789.moveto(3, 9) == True
#     assert t789.pos[0] == 3 and t789.pos[1] == 9
#     assert abs(t789.fuel - 24) < 0.01

#Question 4

# def shortest_continuous_segment(s):
#
#     counter = 1
#     shortest = 9999
#     element = s[0]
#     for i in range(0,len(s)-1):
#         if s[i] == s[i+1]:
#             counter +=1
#         else:
#             if counter < shortest:
#                 shortest = counter
#                 element = s[i]
#                 counter = 1
#             elif counter == shortest:
#                 if s[i] > element:
#                     element = s[i]
#                     shortest = counter
#                     counter = 1
#
#     return element,shortest

#   written
#No mutable data types e.g list in dictionary keys
#Careful integers passed by value will not change the value
#Howeverlists passed by reference so they will change!!

#example

# def reduce_by_1(n):
#
#     n[0] = n[0] - 1
#     n[1] = n[1] - 1
#
# A = (1,2)
# reduce_by_1(A)
# print(A)

# def fiddle(index,lst):
#     index += 1
#     lst[index] += 1
#
# n,nums = 3, range(1,6)
#
# fiddle(n,nums)
# print(n,nums)
#
# def fibrec(n):
#     if n<2:
#         return n
#     else:
#         return fibrec(n-1) + fibrec(n-2)
#
# print(fibrec(6))


#find the nth fibonacci number

def fib(n):
    a = 0
    b = 1
    sum = 0
    for i in range(n):
        # print(a,end=' ')
        sum = a+b
        a = b
        b = sum
    return a
