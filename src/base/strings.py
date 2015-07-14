'''
字符串操作

Created on 2015年2月13日

@author: Administrator
'''

str = "dqsadqzxc231dqasz"
sub = "dq"
s = "abcde"
print(str.count(sub)) # 子串出现的次数
print(str.find(sub))  # 从左开始，查找sub在str中第一次出现的位置。如果str中不包含sub，返回 -1
print(str.index(sub)) # 从左开始，查找sub在str中第一次出现的位置。如果str中不包含sub，举出错误
print(str.rfind(sub)) # 从右开始，查找sub在str中第一次出现的位置。如果str中不包含sub，返回 -1
print(str.rindex(sub))# 从右开始，查找sub在str中第一次出现的位置。如果str中不包含sub，举出错误

print("所有的字符都是字母或数字 : ", str.isalnum())
print("所有的字符都是字母  : ", str.isalpha())
print("所有的字符都是数字 : ", str.isdigit())
print("所有的词的首字母都是大写 : ", str.istitle())
print("所有的字符都是空格 : ", str.isspace())
print("所有的字符都是小写字母 : ", str.islower())
print("所有的字符都是大写字母 : ", str.isupper())

print("字符串从左开始分割 : ", str.split(sub, 1))    # 返回：从左开始，以空格为分割符(separator)，将str分割为多个子字符串，总共分割max次。将所得的子字符串放在一个表中返回。可以str.split(',')的方式使用逗号或者其它分割符
print("字符串从右开始分割 : ", str.rsplit(sub, 1))   # 返回：从右开始，以空格为分割符(separator)，将str分割为多个子字符串，总共分割max次。将所得的子字符串放在一个表中返回。可以str.rsplit(',')的方式使用逗号或者其它分割符

print("字符串拼接 : ", str.join(s)) # 将s中的元素，以str为分割符，合并成为一个字符串

print("去掉位于字符串开头和结尾的sub : ", str.strip(sub))  # 返回：去掉字符串开头和结尾的空格。也可以提供参数sub，去掉位于字符串开头和结尾的sub  
print("字符串替换 : ", str.replace(sub, "dqdq"))  # 返回：用一个新的字符串new_sub替换str中的sub
         
print("将str第一个字母大写 : ", str.capitalize())
print("将str全部字母改为大写 :　", str.upper())
print("将str全部字母改为小写 :　", str.lower()) 
print("将str大写字母改为小写，小写改为大写 : ", str.swapcase())
print("将str的每个词的首字母大写   " + str.title())

 
print(str.center(30))          # 返回：长度为width的字符串，将原字符串放入该字符串中心，其它空余位置为空格。
print(str.ljust(30))           # 返回：长度为width的字符串，将原字符串左对齐放入该字符串，其它空余位置为空格。
print(str.rjust(30))           # 返回：长度为width的字符串，将原字符串右对齐放入该字符串，其它空余位置为空格。

print("字符串格式化")
print("I'm %s. I'm %d year old" % ('jinjinwang', 25))
print("I'm %(name)s. I'm %(age)d year old" % {'name':'jinjinwang', 'age':99})
 
print("%+10x" % 10)
print("%04d" % 5)
print("%6.3f" % 2.3)
print("%.*f" % (4, 1.2))

import this