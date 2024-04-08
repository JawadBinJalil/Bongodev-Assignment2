def are_anagrams(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    
    str1 = str1.replace(" ", "")
    str2 = str2.replace(" ", "")
    
    if len(str1) != len(str2):
        return False
    
    return sorted(str1) == sorted(str2)


string1 = "listen"
string2 = "silent"
if are_anagrams(string1, string2):
    print(f"{string1} and {string2} are anagrams.")
else:
    print(f"{string1} and {string2} are not anagrams.")
