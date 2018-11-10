def isprime(num):
    count=num//2
    if sum([x for x in range(2,count) if num%x==0]):
        return False
    else:
        return True
def factors(num):
    return [x for x in range(1,num+1) if num%x==0]

def primefactor(num):
    factor = []
    lists = factors(num)
    lists = [lists[1], lists[-2]]
   

    for i in lists:
        if isprime(i):
            factor.append(i)
        else:
            factor += primefactor(i)
    return factor

print(primefactor(18))


