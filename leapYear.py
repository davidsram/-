def leap_year(year):
    year=int(year)
    if year%4==0 and year%100!=0:
        print('leap')
    elif year%400==0:
        print('leap')
    else:
        print("no")

if __name__=='__main__':
    leap_year(2000)