import re

def open():
    with open('ptitsi.html','r', encoding = 'utf-8') as f:
        content = f.read()
    return content
def substitute(content):         
    content = re.sub('<.*?>','', content, flags = re.DOTALL) #delete html tags
    content = re.sub(r'(\n| ){2,}','' ,content, flags = re.DOTALL) #delete html tags
    content = re.sub('птиц(а(ми?|х)|ы|е(й|ю)?|у)?','рыб\\1', content)
    content = re.sub('Птиц(а(ми?|х)|ы|е(й|ю)?|у)?','Рыб\\1', content)
    return content
def write(content):
    with open('text.txt','w', encoding = 'utf-8') as f:
        f.write(content)

print(write(substitute(open()))
