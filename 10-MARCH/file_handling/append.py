file=open('jecrc.txt','a+')
# file.write('New line added.')
# file.write('Popular for placement.')
file.writelines([
    'first line \n',
    'Second line \n',
    '3rd line \n'
])
file.seek(0)
print(file.read())
file.close()