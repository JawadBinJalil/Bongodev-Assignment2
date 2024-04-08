def vowels_consonents(sen):
    c1=0
    c2=0
    sentence=sen.lower()
    a='aeiou'
    for char in sentence:
        if char in a:
            c1+=1
        else:
            c2+=1
    
    return c1,c2
                 

st='Hello World'     
vowels,consonents=vowels_consonents(st)
print("Number of Vowels : {}".format(vowels))
print("Number of Consonents : {}".format(consonents))