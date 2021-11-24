import random
from collections import Counter

filename = input()
ENDING = ['.', '!', '?']
f = open(filename, "r", encoding="utf-8")
token = f.read().split()
dictionary, repetitions = {}, {}
for i in range(len(token) - 2):
    double_head = token[i] + ' ' + token[i + 1]
    dictionary.setdefault(double_head, []).append(token[i + 2])
for double_head in dictionary:
    repetitions[double_head] = Counter(dictionary[double_head])
for _ in range(10):
    first_word, last_word = random.choice(list(repetitions.keys())).split()
    while not first_word[0].isupper() or first_word[-1] in ENDING:
        first_word, last_word = random.choice(list(repetitions.keys())).split()
    print(first_word + ' ' + last_word, end='')
    j = 1
    while j < 4 or last_word[-1] not in ENDING:
        j += 1
        rep_w = repetitions[first_word + ' ' + last_word]
        first_word = last_word
        last_word = random.choices(list(rep_w), weights=list(rep_w.values()))[0]
        print(' ' + last_word, end='')
    print()
