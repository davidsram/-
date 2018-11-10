def fib(num):
    a=1
    b=1
    i=0
    if num==1 or num==2:
        print(1)
    else:
        while i<num-2:
            tmp=a
            a=b
            b=tmp+b
            i+=1
        print(b)

fib(6)