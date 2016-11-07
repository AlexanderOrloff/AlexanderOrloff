n = int(input( ))
w = 0
i = 0 
while w <= n:
    w = 2**i
    i += 1                
    if w % 2 == 0 and w <= n:
        print (w)
                    
