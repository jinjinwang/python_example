'''

读取QQ导出的txt格式额聊天记录, 转成数据库所需格式

Created on 2015年3月13日

@author: Administrator
'''

print("读取文件, 保存在集合中")
# 聊天记录
L = []
# 聊天记录数(一个发送时间算一次)
recordsnum = 0
# 聊天记录, 元素是词典
records = []
# 一条聊天记录的内容{'time':'', 'sender':'', 'content':''}
dic = {}
f = open("zhaowei.txt",encoding="utf-8")
for line in f.readlines():
    if len(line.strip()) > 0:
        L.append(line)
    # print(line)
f.close()

print("总共多少行记录 : ", len(L))
# 2014-10-15 13:25:10     2014-12-16 7:58:01

import re
print("将一条聊天记录合并[时间, 人, 内容]")
pattern = re.compile(r'201\d-\d{2}-\d{2}\s[1,2]?\d(:\d{2}){2}')
print("第一条---",L[0])

for i in range(len(L)):
    item = L[i]
    if pattern.match(item):
        print(i,item)
        # 获取时间的下一行记录
        print("recordsnum===", recordsnum, "item--", item);
        nextRecord = L[recordsnum + 1]
        print("next---> " , nextRecord)
        dic = {}
        dic['time'] = item
        dic['sender'] = item
        dic['content'] = nextRecord
        
        records[recordsnum] = dic
        recordsnum = recordsnum + 1
        if recordsnum > 15:
            break
        
print(recordsnum)
print(len(records))
print(records[0])
print(records[1])




