def isprime(num):
    count=num//2
    print([x for x in range(2,count+1) if num%x==0])
    print(sum(x for x in range(2,count+1) if num%x==0))

    if (sum(x for x in range(2,count+1) if num%x==0)):
        print('not prime')
    else:
        print('prime')

isprime(22)