def missing_number(b):
    n = len(b) + 1
    totalsum = (n * (n + 1)) // 2
    actual=sum(b)
    missing_n=totalsum-actual
    return missing_n
    
a = [1, 2, 4, 6, 3, 7, 8] 
print(missing_number(a))