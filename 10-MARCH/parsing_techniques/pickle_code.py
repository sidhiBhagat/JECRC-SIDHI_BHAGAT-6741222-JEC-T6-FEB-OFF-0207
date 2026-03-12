import pickle
file=open('file_1.txt','ab+')
data={
    'fullname':'Siddharth',
    'userid':'siddharth123',
    'password':'*********'
}

enc_data=pickle.dump(data,file)
print(type(enc_data))
ori_data=file.read()
print(ori_data,type(ori_data))
# file.write(enc_data)
file.seek(0)
print(file.read())
dec_data=pickle.load(file)
print(f'Decrypted data : {dec_data}')
file.close()