def common_multiple(a,b):
    if a>b:
        c=a
        while c>0:
            r,c=divmod(a,b)
            a=b;b=c
        print(a)
    elif b>a:
        c=b
        while c>0:
            r,c=divmod(b,a)
            b=a;a=c
        print(b)
    else:
        print(a)

common_multiple(20,27)