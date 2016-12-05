#variant7
quantity = 0
percent = 0
f = open('newy.txt','r',encoding ='utf-8')
for line in f:
    quantity += 1
    a = line.split()
    if len(a) > 5:
        percent += 1
    else:
        continue
    a = []
f.close()        
if percent == 0 or quantity == 0:
    print(' no lines like this')
else:
    print ('the number of lines:', percent / quantity * 100)
