def divide(dollor):
    cent=dollor*100
    dict={}
    for i in (25,10,5,1):
        temp=divmod(cent,i)
        if temp[1]==0:
            dict[i]=temp[0]
            break
        else:
            cent=temp[1]
            dict[i]=temp[0]
    for k,v in dict.items():
        print('%s个%s美分'%(int(v),k))

divide(0.8)