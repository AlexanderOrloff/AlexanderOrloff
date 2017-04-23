import os
def walking():
    d = {}
    for root, dirs, files in os.walk('.'):
        d[root] = len(files)
    maxi = max(d.values())
    for key in d:
        if d[key] == maxi:
            print ('there are',maxi,'files in',key)
walking()
