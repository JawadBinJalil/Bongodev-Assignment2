def Reverse_Words(rev):
    w=rev.split(' ')
    reverse_sentence = ' '.join(reversed(w)) 
    return reverse_sentence

a="Hello World"
print(Reverse_Words(a))
