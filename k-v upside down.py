def upside(d1):
    d2={}
    for i,j in d1.items():
        d2[j]=i
    return d2

d=dict(zip(['ad','sd'],[1,2]))
print(upside(d))