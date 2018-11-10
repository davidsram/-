import random
def random_gen():
    count=random.randint(0,9)
    print(count)
    i=0
    s=set()
    while i<count:
        num=random.randint(0,9)
        s.add(num)
        i+=1
    return s
a=random_gen()
b=random_gen()
print(a|b)
print(a&b)