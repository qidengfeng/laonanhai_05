#!/usr/bin/env python 3.9# coding:utf-8"""Project: 老男孩File: 读写文件.pyCreator: dengfengqiCreate time: 2021-03-07 15:51IDE: PyCharmIntroduction:"""# with open(file="a.txt", mode="rt", encoding="utf-8") as l1:#     print(l1.read())#     print("*" * 10)#     print(l1.read())#t文本r读 w写，a追加写 字符串# with open("a.txt",mode="rt",encoding="utf-8") as f1,\#     open("b.txt",mode="wt",encoding="utf-8") as f2,\#     open("c.txt", mode="at", encoding="utf-8") as f3:#     res=f1.read()#     print(res)#     f2.write(res)#     f3.write(res)# with open("a.txt",mode='rb') as f:#     res = f.read()#     fs=res.decode("utf-8")#     print(fs)# with open("1.py",mode="rb") as f1,open("2.py",mode="wb") as f2:#     res=f1.read()#     print(res)#     app=f2.write(res)#     print(app)# res=[1,2,3]# l=([1,2,3],1,2,3)# print(id(l))# l[0][0]=4# print(l)# print(id(l))with open("a.txt",mode="rb",) as f1:    # f1.seek(2,0)#文件开头    # f1.seek(9,1)#文件当前位置    f1.seek(-3,2)#文件末尾    print(f1.tell())