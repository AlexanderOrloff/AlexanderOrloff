#VARIANT7
import os
import re

def search():
    count = 0
    a =[]
    for f in os.listdir():
        if  os.path.isdir(f) and f not in a:
            #в принципе, так как у меня только папки в задании совпадений не будет, так что массив не очень оправдвн, конечно
            #но потом будет можно при работе с файлами отделить функцией re всё, что до точки
            lat = re.search('.*[a-zA-z].*', str(f))
            rus = re.search('.*[а-яА-ЯЁё].*', str(f))
            if lat != None and rus != None:
                count+=1
                a.append(f)
    if count == 1:
         print('1 dir was found', end = '')
    else:
        print (count, 'dirs were found ', end ='')
    if a != [] :
        print( ':'+', '.join(a))
search()
        
    
