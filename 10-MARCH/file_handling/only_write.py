# # file=open('temp.txt','r')
# file=open('temp1.txt','w')
# # file.write('First file.')
# file.writelines([
#     'first line \n',
#     'Second line \n',
#     '3rd line \n'
# ])

# file.close()


file=open('temp1.txt','w+')
file.writelines([
    'first line \n', 
    'Second line \n',
    '3rd line \n'
])
file.seek(0)
print(file.read())
file.close()