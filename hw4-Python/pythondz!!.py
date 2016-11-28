word = input ('give a word')
lenghth = len(word)
z = 0
newword ='f'
while newword != '':
    newword = ''
    newword = word[z:lenghth]
    print(newword)
    z += 1
    lenghth -= 1      
