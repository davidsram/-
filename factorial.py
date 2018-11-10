import  functools
def factorial(num):
    total=1
    for i in range(1,num+1):
        total*=i

    return total, functools.reduce(lambda x,y:x*y,range(1,num+1))

print(factorial(4))