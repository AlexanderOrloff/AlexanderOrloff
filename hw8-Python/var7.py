#вариант7

import csv
import random

def open_file():
    with open('some.csv', 'r') as f:
        a =[]
        reader = csv.reader(f)
        for line in reader:
            a.append(line)
    return a

def dictionary(a):
    d = {}
    for i in range(0,5):
        d[a[0][i]] = a[1][i]
    return d

def answer(d,a):
    word = random.choice(list(d.values()))
    for key in d:
        if d[key] == word:
            print('твоя подсказка:',key)
    while True:
        ans = input('введи слово')
        if ans == word:
            return random.choice(a[2])
        else:
            print(random.choice(a[3]))
        
print('мы загадали слово для тебя')        
print(answer(dictionary(open_file()),open_file()))

