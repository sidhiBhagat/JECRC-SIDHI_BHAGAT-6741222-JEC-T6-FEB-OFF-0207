## dumps() : Encryption
## loads() : Decryption
## json is used to organize data in a structured way and to exchange data between different programming languages. It is a lightweight data-interchange format that is easy for humans to read and write, and easy for machines to parse and generate. JSON is often used for storing and exchanging data in web applications, APIs, and configuration files.
import json 
file=open('temp.txt','a+')
data={
    'fullname':'Siddharth',
    'userid':'siddharth123',
    'password':'*********'
}
# print(f'Original data : {data}')
# print(f'Type of original data : {type(data)}')
# print()
enc_data=json.dumps(data)
print(type(enc_data))

ori_data=file.read()
print(ori_data,type(ori_data))
# print(f'Encrypted data : {enc_data}')
# print(f'Type of encrypted data : {type(enc_data)}')
# print()
# dec_data=json.loads(enc_data)
# print(f'Decrypted data : {dec_data}')
# print(f'Type of decrypted data : {type(dec_data)}')
file.write(enc_data)
file.seek(0)
print(file.read())
file.close()
