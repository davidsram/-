def ispeferct(num):

    digit_sum=sum(x for x in range(1,num) if num%x==0)
    if digit_sum==num:
        print('perfect')

ispeferct(6)