def step_increment():
    a=[]
    f=int(input('from'))
    t=int(input('to'))
    i=int(input('increment'))
    for i in range(f,t+1,i):
        a.append(i)
    print(a)

print(type(range(12,23)))
step_increment()