#!/usr/bin/env python 3.9# coding:utf-8"""Project: 老男孩File: 解压赋值.pyCreator: dengfengqiCreate time: 2021-02-28 11:42IDE: PyCharmIntroduction:解压赋值"""# list_=[1,2,3,4]#列表# str_="Introduction"#字符串# dict_={"Project": "老男孩",#字典取key# "File": "解压赋值.py",# "Creator": "dengfengqi"}# a,b,c,*_=dict_# print(a,b,c)# #字符串# res="hello world"## print(res.replace("h", "戚登锋"))# print(res.rsplit("ll"))#替换并以此字符为分割，返还列表# print(res.lower())list_=[1,2,3,4]#列表# print(list_.pop(0))#根据索引删除，并返回删除的数据print(list_.remove(1),list_)#根据数值删除无返回值