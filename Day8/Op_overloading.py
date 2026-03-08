class MyDataType:
    def __init__(self, value):
        self.value = value
    def __add__(self, other_obj):
        return self.value + other_obj.value
obj1 = MyDataType(10)
obj2 = MyDataType(20)
print(obj1 + obj2)  # This will raise a TypeError