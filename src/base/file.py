'''
f = open("record.txt","w")
f.write("tom, 12, 86\n")
f.write("Lee, 15, 99\n")
f.write("Lucy, 11, 58\n")
f.write("Joseph, 19, 56")
f.close()
'''
f = open("record.txt","r")
#content1 = f.readlines()
#print(content1)
content2 = f.read()
print(content2)
f.close()
