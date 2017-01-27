#(буд(ут?|е(шь|те?|м|)) )?
import re
def open_text():
    words = []
    with open('text.txt', 'r', encoding ='utf-8') as f:
        text = f.read().lower()
        text = text.split()
        for item in text:
            item = item.strip('.,?!-')
            if item not in words:
                words.append(item)
    return words

def answer(words):
    for item in words:
        m = re.match( r'\bси(д(и(шь|те?|м)?|е(л(о|а|и)?|в(ш(и(й|ми?|е|х)?|е(го|му?|е|й|ю)|ая|ую))?|ть)|я(т|щ(и(й|ми?|е|х)|е(го|му?|е|й|ю)|ая|ую))?)|жу)\b', item)
        if m != None:
            print(item)

sit = answer(open_text())

#можно сделать отдельную функцию на будущее время, которая будет искать, вырезать и печатать потом найденную форму буду + сидеть(всегда)
