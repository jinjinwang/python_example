'''
Created on 2015年1月15日

@author: Administrator
'''

dic = {'tom':11, 'sam':57,'lily':100}
# 类型
print(type(dic))

# 获取词典元素
print(dic['tom'])

# 修改词典
dic['tom'] = 30
print(dic)

# 新增元素
dic['lilei'] = 99
print(dic)

# 词典置空
dic = {}
print(dic)

#词典循环
dic = {'lilei': 90, 'lily': 100, 'sam': 57, 'tom': 90}
for key in dic:
    print (dic[key])

#删除元素    
del dic['tom']
print(dic)

#词典长度
print(len(dic))