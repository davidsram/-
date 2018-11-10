def m_add(a,b):
    i=0
    j=0
    if len(a)==len(b) and len(a[0])==len(b[0]):
        c = []
        for i in range(len(a)):
            m=[]
            for j in range(len(a[0])):
                d=a[i][j]+b[i][j]
                m.append(d)
            c.append(m)

    else:
        print(r"metrix can't calculate")

    print(c)



def madd(M1, M2):

    if isinstance(M1, (tuple, list)) and isinstance(M2, (tuple, list)):

        return [[m+n for m,n in zip(i,j)] for i, j in zip(M1,M2)]




def multi(M1, M2):

    if isinstance(M1, (float, int)) and isinstance(M2, (tuple, list)):

        return [[M1*i for i in j] for j in M2]

    if isinstance(M1, (tuple, list)) and isinstance(M2, (tuple, list)):

        return [[sum(map(lambda x: x[0]*x[1], zip(i,j)))for j in zip(*M2)] for i in M1]#zip(*m2)转置m2矩阵



a=((1, 2,3), (1, 4, 9),(1, 1, 1),(0, 0, 0))
b=a
# m_add(a,b)
# print(madd(a,b))
for i in zip(*a):
    print(i)
print(zip(*a))
x,y,z=zip(*a)
print(x,y,z)
print(multi(a,b))