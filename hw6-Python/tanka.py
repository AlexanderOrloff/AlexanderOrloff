#вариант7
#Текст должен представлять собой танка, то есть стихотворение на русском языке из пяти строк без рифмы, при этом длина первой строки должна быть 5 слогов,
#второй строки - 7 слогов, третьей строки - 5 слогов, четвёртая и пятая строка - по 7 слогов. Количество предложений в таком тексте может быть любым.
import random
def imperative():
    with open('imperatives.txt', 'r',encoding = 'utf-8') as f:
        imperatives =[]
        for line in f:
            newword = line.strip()
            imperatives.append(newword)
        return random.choice(imperatives)
def noun_acc():
    with open('nouns_Acc_Sg&Pl.txt', 'r',encoding = 'utf-8') as f:
        noun_accs =[]
        for line in f:
            newword = line.strip()
            noun_accs.append(newword)
        return random.choice(noun_accs)
def ins_phrase():
    with open('clitics_Ins.txt', 'r',encoding = 'utf-8') as f:
        clitics = []
        for line in f:
            newword = line.strip()
            clitics.append(newword)
    
    with open('nouns_Ins.txt', 'r',encoding = 'utf-8') as g:
        noun_inss = []
        for line in g:
            newword = line.strip()
            noun_inss.append(newword)
    return random.choice(clitics) + ' ' + random.choice(noun_inss)
def noun_pl():
    with open('nouns_ Nom=Acc_Pl.txt', 'r',encoding = 'utf-8') as f:
        noun_pls = []
        for line in f:
            newword = line.strip()
            noun_pls.append(newword)
        return random.choice(noun_pls)    
def noun_sg():
    with open('nouns_Nom=Acc_Sg.txt', 'r',encoding = 'utf-8') as f:
        noun_sgs = []
        for line in f:
            newword = line.strip()
            noun_sgs.append(newword)
        return random.choice(noun_sgs)
def verb():
    with open('verbs_Pl.txt', 'r',encoding = 'utf-8') as f:
        verbs = []
        for line in f:
            newword = line.strip()
            verbs.append(newword)
        return random.choice(verbs)
def adverb():
    with open('adverbs.txt', 'r',encoding = 'utf-8') as f:
        adverbs = []
        for line in f:
            newword = line.strip()
            adverbs.append(newword)
        return random.choice(adverbs)
def punctuation():
    marks = ['.', '!', '...']
    return random.choice(marks)
def type1():
    return imperative() + ' ' + noun_acc() + punctuation()
def type2():
    return noun_pl() + ' ' + verb() + punctuation()
def type3():
    return imperative() + ' ' + ins_phrase() + punctuation()
def type4():
    return noun_pl() + ' ' + verb() + ' ' + noun_pl() + punctuation()
def type5():
    return noun_pl() + ' ' + verb() + ' ' + noun_sg() + punctuation()
def type6():
    return ins_phrase() + ' ' + imperative() + ' ' + noun_sg() + punctuation()
def type7():
    return imperative() + ' ' + noun_acc() + ' ' + adverb() + punctuation()
def tanka(i):
    line =''
    if (i == 1) or (i == 3):
        line = random.choice([1,2,3])
        if line == 1:
            line = type1()
        if line == 2:
            line = type2()
        if line == 3:
            line = type3()
    else:
        line = random.choice([4,5,6,7])
        if line == 4:
            line = type4()
        if line == 5:
            line = type5()
        if line == 6:
            line = type6()
        if line == 7:
            line = type7()
    return line               
def printing():
    for i in range(1,6):
        print(tanka(i))
a = printing()    
    

