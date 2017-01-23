import csv
import random
def open_file():
    a = []
    with open('some.csv', 'r') as f:
        reader = csv.reader(f)
        for line in reader:
            a.append(line)
    d = {}
    for i in range(0,5):
        d[a[0][i]] = a[1][i]
    return a
def answer(a):
    print('мы загадали слово для тебя')
    word = random.choice(a)
    

print(answer(open_file))
