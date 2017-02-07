import re
def open_text():
    with open('archi.html','r', encoding = 'utf-8') as f:
        text = f.read()
    return text

def search(text):
    m = re.search(r'title="Коды языков".*?title="ISO (\d\d\d)"',text, flags = re.DOTALL)
    return m.group(1)

def write(z):
    with open('archi.txt','w', encoding = 'utf-8') as f:
        f.write(z)
archi = write(search(open_text()))
