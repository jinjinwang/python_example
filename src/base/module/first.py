'''
Created on 2015年1月15日

@author: Administrator
'''

def laugh():
    print ('HaHaHaHa')
    
def lib_func(a):
    return a + 10

def lib_func_another(b):
    return b + 20

# 测试语句可以写在此处, 该模块被import时不会执行
# 当直接运行first.py时，__name__为"__main__"。如果被import的话，__name__为"first"。
if __name__ == '__main__':
    test = 101
    print(lib_func(test))