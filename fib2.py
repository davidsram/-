def fib(max):
    n, a, b = 0, 0, 1
    c=[]
    while n < max:
        print (b)
        c.append(b)
        (a, b) = (b, a + b)
        n = n + 1

    print(c)
    print(sum(c))
    return 'done'
fib(6)