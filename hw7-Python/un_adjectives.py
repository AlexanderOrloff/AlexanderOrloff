# вариант7
def open_text(text):
    with open(text, 'r', encoding ='utf-8') as f:
        text = f.read().lower()
        words = text.split()
    return words

def percent(words, number):
    i,j = 0,0
    for item in words:
        if item[0:2] =='un':
            i+=1
            if len(item) > number:
                j +=1   
    if i != 0:
        return round(j / i * 100)
    else:
        return 'no matching words were found'

def questions():
    text = input(' Please, enter the name of the text')
    number = int(input(' Please, enter the lenght'))
    words = open_text(text)
    answer = percent(words, number)
    return answer

print(questions())
    
