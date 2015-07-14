'''
Created on 2015年1月22日

@author: Administrator
'''

for line in open('record.txt'):
    print (line)
    
    
def gen():
    a = 100
    yield a
    a = a*8
    yield a
    yield 1000

for i in gen():
    print (i)
    
def gen1():
    for i in range(4):
        yield i
        
for i in gen1():
    print (i)

L = []
for x in range(10):
    L.append(x**2)
print(L)

xl = [1,3,5]
yl = [9,12,13]
L  = [ x**2 for (x,y) in zip(xl,yl) if y > 10]
print(L)  
    