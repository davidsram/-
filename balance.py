balance=int(input('balance'))
payment=int(input('payment'))
i=0
while (balance-payment)>0:
    i+=1

    balance=balance-payment
    print(i,balance,payment)

else:
    i=i+1
    payment=balance
    print(i,balance,payment)
