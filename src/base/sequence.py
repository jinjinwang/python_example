'''
序列(表，定值表，字符串)

Created on 2015年2月12日

@author: Administrator
'''

test = "0123654789963"
print(min(test)) # 序列中最小的元素
print(max(test)) # 序列中最大的元素

print(test.count('3')) # x在s中出现的次数
print(test.index('3')) # x在s中第一次出现的下标

l1 = [1,3,5]
l2 = [2,4,6,8]
print(l1)
print(sum(l1)) # 返回序列中所有元素的和
l1.extend(l2)  # 在表l的末尾添加表l2的所有元素
print(l1)
l1.append(10) # 在l的末尾附加x元素
print(l1)
l1.sort() # 对l中的元素排序
print(l1)
l1.reverse() # 将l中的元素逆序
print(l1)
print(l1.pop()) # 返回：表l的最后一个元素，并在表l中删除该元素
print(l1)
del l1[2] # 删除该元素
print(l1)



