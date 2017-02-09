import re

def substitute():
    with open('ptitsi.html','r', encoding = 'utf-8') as f:
        content = f.read()
    content = re.sub('<.*?>','', content, flags = re.DOTALL) #delete html tags
    content = re.sub(r'(\n| ){2,}','' ,content, flags = re.DOTALL) #delete html tags
    content = re.sub('птиц(а(ми?|х)|ы|е(й|ю)?|у)?','рыб\\1', content)
    content = re.sub('Птиц(а(ми?|х)|ы|е(й|ю)?|у)?','Рыб\\1', content)
    return content

print(substitute())
