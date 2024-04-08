
def c_Occurrences(l):
    count={}
    for i in l:
        if i in count:
            count[i]+=1
        else:
            count[i]=1
    return count

List = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
print(c_Occurrences(List))