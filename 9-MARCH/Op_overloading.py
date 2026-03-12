# class MyDataType:
#     def __init__(self, value):
#         self.value = value
#     def __add__(self, other_obj):
#         return self.value + other_obj.value
# obj1 = MyDataType(10)
# obj2 = MyDataType(20)
# print(obj1 + obj2)  # This will raise a TypeError

'''
class ClassName:
    def __init__(self, value):
        self.value = value
    def __add__(self, other_obj):
        return self.value + other_obj.value
    
obj1 = ClassName(10)
obj2 = ClassName(20)
print(obj1 + obj2)
# obj1.__add__(obj2)
'''

class MyDT:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

    def __add__(self, *args):
        sum = self.value
        for i in args:
            sum += i.value
        return MyDT(sum)
    
    # def add(self, *args):
    #     sum = self.value
    #     for i in args:
    #         sum += i.value
    #     return sum

    def __sub__(self, *other_obj):
        diff = self.value
        for i in other_obj:
            diff -= i.value
        return MyDT(diff)

    def sub(self, *args):
        diff = self.value
        for i in args:
            diff -= i.value
        return diff

    def __mul__(self, other):
        return self.value * other.value
    def __floordiv__(self, other):
        return self.value // other.value
    def __truediv__(self, other):
        return self.value / other.value
    def __mod__(self,other):
        return self.value % other.value
    
    
print(MyDT(10.10)+MyDT(20)+MyDT(30)+MyDT(40))

# print(MyDT.add(MyDT(10.10), MyDT(20), MyDT(30.7), MyDT(40)))
# print(MyDT.sub(MyDT(100), MyDT(20), MyDT(30), MyDT(40)))



print(MyDT(100)-MyDT(20)-MyDT(30))
# print(MyDT(11)*MyDT(20))
# print(MyDT(70.0)/MyDT(20))
# print(MyDT(100)%MyDT(50))
# print(MyDT(100)//MyDT(50))