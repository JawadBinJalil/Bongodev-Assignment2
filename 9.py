def remove_duplicates(lst):
    if not lst:
        return 0
    
    new_length = 1
    for i in range(1, len(lst)):
        if lst[i] != lst[i - 1]:
            lst[new_length] = lst[i]
            new_length += 1
            
    return new_length

lst = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
length_without_duplicates = remove_duplicates(lst)
print("Length of array : {}".format(length_without_duplicates))
print("Array without duplicates : {}".format(lst[:length_without_duplicates]))

