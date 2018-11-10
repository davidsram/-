def findchr(string_in,char):
    num=len(string_in)-1
    i=0
    while i<num:
        if string_in[i]==char:
            print(i)
            break
        i+=1
    else:
        print(-1)

def rfindchr(string_in,char):
    num = -len(string_in)
    i=-1
    while i>=num:
        if string_in[i]==char:
            print(-num+i)
            break
        i=i-1
    else:
        print(-1)

findchr('afd','f')
rfindchr('qeqrwf','q')