'''
练习题二
计算下面一段文字里面所有字母出现次数
I can show you the world.Shining, shimmering, splendid
Tell me, princess, now when did You last let your heart decide?
I can open your eyes.Take you wonder by wonder
Over, sideways and under On a magic carpet ride

Created on 2015年2月10日

@author: Administrator
'''
a = '''I can show you the world.Shining, shimmering, splendid
Tell me, princess, now when did You last let your heart decide?
I can open your eyes.Take you wonder by wonder
Over, sideways and under On a magic carpet ride 
'''
from functools import reduce

a = a.lower();
print(a)
lst = list(a)
print(len(lst))
dic = {}
for letter in lst : 
    if letter.isalpha() :
        if letter not in dic.keys():
            dic[letter] = 1
        else:
            dic[letter] = dic.get(letter) + 1
print(dic)

print(reduce((lambda x,y : x+y), dic.values()))





    
