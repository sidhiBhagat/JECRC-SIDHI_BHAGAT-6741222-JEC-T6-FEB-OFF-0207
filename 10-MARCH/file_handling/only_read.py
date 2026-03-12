file=open("temp1.txt",'r')

# # print(file.read())

print(file.readline())
print(file.readline())
print(file.readline())
# print(file.readlines())

# file.close()
file.seek(0)
# file=open('notes.txt','r')
# print(file.read())
print(file.readlines())
file.close()