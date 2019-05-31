# -*- coding: utf-8 -*-
# @Time    : 2019/5/28 18:21
# @Author  : Weiyang
# @File    : util.py
'''
从 小黄鸡对话.conv 抽取出对话数据,
并存放于../source文件夹里
'''

filepath = './小黄鸡对话.conv'
# source 端数据
source = []
# target 端数据
target = []
with open(filepath,'r',encoding='utf-8') as fi:
    temp = []
    for line in fi:
        if line.startswith('E'):
            temp = []
            temp.append(line)
        if line.startswith('M') and len(temp) <= 3:
            line = line.lstrip('M').strip()
            temp.append(line)
        if len(temp) == 3:
            source.append(temp[1])
            target.append(temp[2])
assert len(source) == len(target),'source端数据和target端数据个数不一致'
# 分割数据为训练集，评估集和测试集
num = len(source)
# 训练集
with open('../source/train/source.txt','w',encoding='utf-8') as fs,open('../source/train/target.txt','w',encoding='utf-8') as ft:
    for i in range(int(num*0.7)):
        fs.write(source[i]+'\n')
        ft.write(target[i]+'\n')
print('Train Done!')
# 评估集
with open('../source/eval/source.txt','w',encoding='utf-8') as fs,open('../source/eval/target.txt','w',encoding='utf-8') as ft:
    for i in range(int(num*0.7),int(num*0.75)):
        fs.write(source[i]+'\n')
        ft.write(target[i]+'\n')
print('Eval Done!')
# 测试集
with open('../source/test/source.txt','w',encoding='utf-8') as fs,open('../source/test/target.txt','w',encoding='utf-8') as ft:
    for i in range(int(num*0.75),num):
        fs.write(source[i]+'\n')
        ft.write(target[i]+'\n')
print('Test Done!')