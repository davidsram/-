def redPot(num,target):
    i=0
    flag=False
    if type(num)!=int:
        print(len(num))
        while i<len(num):
            if num[i]>10 and num[i+1]>10:
                flag=True
                break
            i+=1
        if sum(num)>=target and flag :
            return  'true'
        else:
            return 'false'
    else:
        return 'false'

num=input('支付记录')
target=input('目标金额')
num=eval(num)
target=eval(target)
print(redPot(num,target))