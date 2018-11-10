#coding:utf-8
#得到一个用户输入
num_str = input('Enter a number: ')

#将用户输入的数字字符转化成int类型
num_num = int(num_str)

#创建一个1~用户输入数字的列表
fac_list = list(range(1, num_num + 1))
print ("Before:",fac_list)

# 定义一个整型变量并赋值为0
i = 0
deleted = []

# while循环判断条件
while i < len(fac_list):
    # 用户输入数字对里表中index 为i的数字求余.
    if num_num % fac_list[i] == 0:
        #修改此处.
        del fac_list[i]
        i=i-1
        # deleted.append(fac_list[i])
    # 变量自增.
    i = i + 1
for ch in deleted:
    fac_list.remove(ch)

print("After:", fac_list)