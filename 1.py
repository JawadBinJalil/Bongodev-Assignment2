def Fibonacci(n):
    a=0
    b=1
    for i in range(1,n+1):
        print(a)
        result=a+b
        a=b
        b=result
        
Fibonacci(int(input()))