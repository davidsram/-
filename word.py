a=input('first')
b=input('second')
a=list(a)
b=list(b)
if len(a)==len(b):
    for x in a:
        b.remove(x)
    if len(b)==0:
        print('yes')
    else:
        print('no')
else:
    print('no')