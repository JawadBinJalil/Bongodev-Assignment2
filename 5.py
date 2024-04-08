def is_palindrom(sen):
    s=sen.lower()
    clean_s = ''
    for char in s:
        if char.isalnum():
            clean_s += char.lower()
    return clean_s==clean_s[::-1]
            
sentence = "A man, a plan, a canal, Panama"
if is_palindrom(sentence):
    print("It is Palindrom")
else:
    print("Not Pelindrom")
