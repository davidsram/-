def max_letter(str_my):
    if isinstance(str_my, str):
        str_my = str_my.lower().replace(' ', '')
        cou={}
        letter=[]
        for i in str_my:
            cou[i]=str_my.count(i)
        print(cou)
        max_value = max(cou.values())

        for k, v in cou.items():
            if v == max_value:
                letter.append(k)
        print('max letter\'s number:',max_value)
        print('the letter is:',letter)
    else:
        print('type again')
max_letter('it\'s very good')
