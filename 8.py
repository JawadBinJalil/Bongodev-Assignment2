def duplicate(l):
    dup_list=[]
    u_list=[]
    for i in l:
        if i not in u_list:
            u_list.append(i)
        elif i not in dup_list:
            dup_list.append(i) 

    
    return dup_list 
    
List = [1, 2, 3, 2, 4, 5, 4, 6]
dl=duplicate(List)
print(dl)
