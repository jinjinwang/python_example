'''
Created on 2015年3月2日

@author: Administrator
'''

print("查询对象的属性")
a = [1,2,3]
print(hasattr(a,'append'))

print("查询对象所属的类和类名称")
print(a.__class__)
print(a.__class__.__name__)

print("查询父类")
print(list.__base__)

#coding=utf8
print("使用中文")
print("你好吗?你好吗？")

#-*- coding: UTF-8 -*-
print("你好吗？")

print("表示2进制，8进制和16进制数字")
print(0b1110)     # 二进制，以0b开头
print(0o10)       # 八进制，以0o开头
print(0x2A)       # 十六进制，以0x开头

print(int("1110", 2))
print(int("10", 8))
print(int("2A", 16))

print("搜索路径")
import sys
print(sys.path)


