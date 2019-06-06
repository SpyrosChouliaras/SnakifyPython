# Dictionaries
# 1.  Number of occurrences

dict = dict()
string = input()
for word in string.split():
    dict[word] = dict.get(word, 0) + 1
    print(dict[word] - 1, end=' ')

# 2.Dictionary of synonyms

dict = {}
n = int(input())
for i in range(n):
    word1, word2 = input().split()
    dict[word1] = word2
    dict[word2] = word1
print(dict[input()])

# (3.) Elections in the USA
dict = {}
n = int(input())
for i in range(n):
    candidate, vote = input().split()
    vote = int(vote)
    dict[candidate] = dict.get(candidate, 0) + int(vote)

for values, keys in sorted(dict.items()):
    print(values, keys)

# 3. Access rights

dict1 = {"read": "R", "write": "W", "execute": "X"}
dict2 = {}

for i in range(int(input())):
    file, *perm = input().split()
    dict2[file] = set(perm)

for j in range(int(input())):
    operation, file = input().split()
    if dict1[operation] in dict2[file]:
        print("OK")
    else:
        print("Access denied")

# (4.) Countries and cities

dict1 = {}

for i in range(int(input())):
    country, *cities = input().split()
    for elem in cities:
        dict1[elem] = country

print(dict1)
for j in range(int(input())):
    print(dict1[input()])

# 4.Frequency analysis

dict1 = {}
for i in range(int(input())):
    string = input()
    for word in string.split():
        dict1[word] = dict1.get(word, 0) + 1

sort_by_values = [(-count, word) for (word, count) in dict1.items()]
for i, j in sorted(sort_by_values):
    print(j)

# 5.English-Latin dictionary

from collections import defaultdict

latin_to_english = defaultdict(list)
for i in range(int(input())):
    english_words, latin_words = input().split(' - ')
    latin_words_sep = latin_words.split(', ')
    for words in latin_words_sep:
        latin_to_english[words].append(english_words)

print(len(latin_to_english))
for words, english_translations in sorted(latin_to_english.items()):
    print(words + ' - ' + ', '.join(english_translations))
