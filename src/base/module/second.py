'''
Created on 2015年1月15日

@author: Administrator
'''
#第一种引入方式
# import first
# 
# for i in range(10):
#     first.laugh()


# 第二种引入方式
# import first as b
# for i in range(10):
#     b.laugh()

# from first import laugh
# for i in range(10):
#     laugh()

#第四种引入方式    
# from first import *
# for i in range(10):
#     laugh()

import first
print(first.lib_func(120))

import inspect
print("查询函数的参数")
print(inspect.getargspec(first.lib_func))

