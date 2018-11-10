# def tr(src,dst,string):
#     # if src in string:
#     #     print('in')
#     #     index=string.index(src)
#         string = string.replace(src,dst)
#         return string
#
# print(tr('as','dkkf','asdfg'))

# -*- coding:utf-8 -*-

# 2015-04-05


def tr(srcstr, dststr, mystring, flag=True):
    src_dst = {}

    newstring = ''

    if len(srcstr) == len(dststr):

        '''(a)和(b)的前两问'''

        if flag:

            for key, value in zip(srcstr, dststr):
                src_dst.setdefault(key, value)

            for i in mystring:

                if i in src_dst:

                    newstring += src_dst[i]

                else:

                    newstring += i

        else:

            for key, value in zip(srcstr.lower(), dststr):
                src_dst.setdefault(key, value)

            for i in mystring:

                if i.lower() in src_dst:

                    newstring += src_dst[i.lower()]

                else:

                    newstring += i

    else:

        '''(c)删除字符的功能'''

        if flag:

            for key, value in zip(srcstr[:len(dststr)], dststr):
                src_dst.setdefault(key, value)

            for i in mystring:

                if i in src_dst:

                    newstring += src_dst[i]

                elif i not in srcstr:

                    newstring += i

        else:

            for key, value in zip(srcstr.lower()[:len(dststr)], dststr):
                src_dst.setdefault(key, value)

            for i in mystring:

                if i.lower() in src_dst:

                    newstring += src_dst[i.lower()]

                elif i not in srcstr:

                    newstring += i

    return newstring


if __name__ == '__main__':
    srcstr = input('Please input srcstr:')

    mystring = input('Please input the string:')
    dststr = input('Please input dststr:')

    flag = input('Lower or uppper,input True or False:')  # 是否区分大小写的参数

    newstring = tr(srcstr, dststr, mystring, flag)

    print(newstring)

