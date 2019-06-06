# SETS
# 1.The number of distinct numbers
print(len(set(input().split())))

# 2.The number of equal numbers

print(len(set(input().split()) & set(input().split())))

# 3.The intersection of sets

count1 = set(input().split())
count2 = set(input().split())

inter = sorted(count1.intersection(count2))

print(' '.join(inter))

# (4.)Has the number been encountered before

list = [int(i) for i in (input().split())]
set = set()
for num in list:
    if num in set:
        print("YES")
    else:
        print("NO")
        set.add(num)

# 4. Cubes


def print_set(set):
    print(len(set))
    print(*[str(y) for y in sorted(set)])


N, M = [int(x) for x in input().split()]
set1, set2 = set(), set()
for i in range(N):
    set1.add(int(input()))
for j in range(M):
    set2.add(int(input()))

print_set(set1 & set2)
print_set(set1 - set2)
print_set(set2 - set1)

# (6.) The number of distinct words in some text

n = int(input())
set1 = set()
for i in range(n):
    set1.update(input().split())

print(len(set1))

# 5.Guess the number
n = int(input())
numbers = set(range(n))
possible_numbers = numbers
while True:
    guess = input()
    if guess == "HELP":
        break
    guess = {int(x) for x in guess.split()}
    answer = input()
    if answer == "YES":
        possible_numbers &= guess
    elif answer == "NO":
        possible_numbers &= possible_numbers - guess

print(' '.join([str(x) for x in sorted(possible_numbers)]))

# 6. Polyglots

students = int(input())
student_language = set()
all_languages = list()
for i in range(students):
    lang_numb = int(input())
    for j in range(lang_numb):
        student_language.add(str(input()))
    all_languages.append(student_language)
    student_language = set()

known_by_all, known_by_someone = set.intersection(*all_languages), set.union(*all_languages)

print(len(known_by_all), *sorted(known_by_all), sep='\n')
print(len(known_by_someone), *sorted(known_by_someone), sep='\n')
