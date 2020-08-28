# Sentence reversal

def reverse_list(l):
    start = 0
    end = len(l)-1
    while start<end:
        l[start],l[end] = l[end],l[start]
        start+=1
        end-=1
    return l

def sentence_rev(sentence):
    space = [' ']
    words = []
    i=0
    length = len(sentence)
    while i<length:
        if sentence[i] not in space:
            word_start = i
            while i<length and sentence[i] not in space:
                i+=1
            words.append(sentence[word_start:i])
        i+=1
    return ' '.join(reverse_list(words))


#driver code
sentence = "here is what I have to say"
print(sentence_rev(sentence))
