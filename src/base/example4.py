'''

内置函数

Created on 2015年3月4日

@author: Administrator
'''

code1 = compile("print('Hello')",'example4.py','exec')  # 编译字符串成为code对象
print(eval("1 + 1"))                     # 解释字符串表达式。参数也可以是compile()返回的code对象
exec("print('Hello')")            # 解释并执行字符串，print('Hello')。参数也可以是compile()返回的code对象
exec(code1)
