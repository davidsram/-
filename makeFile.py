'creat text file'

import os
ls=os.linesep
fname='as'
while True:

    if os.path.exists(fname):
        print('error:%s'%fname)
    else:
        break

all=[]
print('\nenter lines(\'.\'to quit).\n')

while True:
    entry=input('>')
    if entry=='.':
        break
    else:
        all.append(entry)

fobj=open(fname,'w')
fobj.writelines(['%s%s' %(x,ls)for x in all])
fobj.close()