'''
函数参数的使用
Created on 2015年1月15日

@author: Administrator
'''

def f(a,b,c):
    return a*b+c

#位置传递
print(f(1,2,3))

#关键字传递
print(f(c=3,b=2,a=1))

#关键字和位置混合
print(f(1,c=3,b=2))

#参数默认值
def f1(a,b,c=10):
    return a+b+c

print(f1(3,2))
print(f1(3,2,1))

#包裹传递元组
def func(*name):
    print (type(name))
    print (name)

func(1,4,6)
func(5,6,7,1,2,3)

#包裹传递字典
def func2(**dicts):
    print (type(dicts))
    print (dicts)

func2(a=1,b=9)
func2(m=2,n=1,c=11)

#解包裹传递参数
def func3(a,b,c):
    print (a,b,c)

args = (1,3,4)
func3(*args)

dicts = {'a':1,'b':2,'c':3}
func3(**dicts)

'这里为什么打印的是a b c'
func3(*dicts)