#variant7
import re 
def sentences():
    with open ('text.txt','r',encoding = 'utf-8') as f:
        text = f.read()
        m = re.findall('[^.!?]{1,}?[.?!]', text)
        m= [sent.split() for sent in m]
        for sentence in m:
            for i in range(len(sentence)):
                sentence[i] = sentence[i].strip('!?.,;:"').lower()
        return m

def output(m):
    maxi = max([len(word) for sentence in m for word in sentence])
    sentence_number = 0
    for sentence in m:
        sentence_number += 1
        print ('предложение №', sentence_number)
        words = []
        for word in sentence:
            if word not in words:
                words.append(word)
                j = 0
                for i in range(0, len(sentence) - 1):
                    if word == sentence[i]:
                        j += 1
                if j  > 1:
                        print('{:^{maxi}} {:^2}'.format(word,j, maxi = maxi))
                
output(sentences())

