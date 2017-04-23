import os
def walking():
    d = {root : len(files) for root, dirs, files in os.walk('.')}
    maxi = max(d.values())
    for key in d:
        if d[key] == maxi:
            print ('there are',maxi,'files in',key)
walking()
