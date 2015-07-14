'''
练习题一
输出数字，从1到100，其中能被3整除的，显示‘buzz’，其中能被5整除的，显示‘bing’，既能被3整除又能被5整除的，输出‘buzz*bing’

Created on 2015年2月10日

@author: Administrator
'''
i = 0
while i <= 100:
    i = i + 1
    if i%3 == 0 and i%5 == 0:
        print(i,"----buzz*bing")
        continue
    if i%3 == 0:
        print(i,"----buzz")
        continue
    if i%5 == 0:
        print(i,"----bing")
        continue
    
