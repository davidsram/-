import time
import re
db={'yu':[123,2134.12]}
print(type(time.time()))
def login():
    name=input("name:").lower()
    pwd=int(input('password'))
    print(re.match(r'\w',name))
    if name in db and pwd==db[name][0]:
        print('login sucess')
        if time.time()-int(db[name][1])<4*3600:
            # pass
            print('logged in at ',time.asctime(time.localtime(db[name][1])))
        db[name][1]=time.time()
        print(db)

login()
login()