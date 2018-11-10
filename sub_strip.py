#coding:utf-8
str1 =input("Enter a string -->")
while (str1[0]==' ') or (str1[-1]==' '):

    if str1[0] == ' ':
        if str1[-1] == ' ':
            str1 = str1[1:-1]
        else:
            str1 = str1[1:]
    elif str1[-1] == ' ':
        str1 = str1[:-1]

print(str1,len(str1))