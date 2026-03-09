'''
Example for public Access specifier.
'''
# class Temp:
#     a,b,*c,d='HELLO'

#     def greeting(self):
#         print('Good Afternoon users!')

# class C2(Temp):
#     pass

# c=C2()
# print(c.c)
# print(Temp.a)

'''Example for protected Access specifier.'''

# class Temp:
#     _a=10
#     _b='I LOVE PYTHON'

# obj=Temp()
# print(obj._a)
# print(obj._b)

'''Example for private Access specifier.'''

# class Temp:
#     __a=100

#     def __status (self):
#         print('This is a private method')

# obj=Temp()
# print(obj.__a)
# obj.__status()


'''
1. By using syntax
2. Get & set methods 
3. By using @property decorater(setter)

'''
## By using Syntax
'''
print(obj._Temp__a)
print(Temp._Temp__a)

obj._Temp__status()

def new_method():
    print("Method definition got changed.")

obj._Temp__a= '123456789'
obj._Temp__status = new_method
print(obj._Temp__a)
obj._Temp__status()
'''

## By using get & set methods
'''
class Temp:
    __a=100

    def __status (self):
        print('This is a private method')

    def get(self):
        return self.__a

    def set(self, new_val):
        self.__a = new_val

obj=Temp()
obj.get()
# obj.set(12)
# obj.get()
print(obj._Temp__a)
'''


## By using @property decorator
'''
class Temp:
    __a =10
    @property
    def get(self):
        print(self.__a)
    @get.setter
    def set(self, new_val):
        self.__a=new_val

obj=Temp()
obj.get
obj.set=10000
obj.get
print(obj._Temp__a)
'''
