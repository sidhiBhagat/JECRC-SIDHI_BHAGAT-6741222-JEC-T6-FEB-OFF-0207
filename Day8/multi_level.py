class Class1:  # parent class
    a='class_1'
    def method1(self):
        print("This is method 1 of Class1")

class Class2(Class1):
    b='class_2'
    def method2(self):
        print("This is method 2 of Class2")

class Class3(Class2):
    c='class_3'
    def method3(self):
        print("This is method 3 of Class3")

class Class4(Class3):
    d='class_4'
    def method4(self):
        print("This is method 4 of Class4")

class Class5(Class4):
    e='class_5'
    def method5(self):
        print("This is method 5 of Class5")

obj=Class5()
print(obj.a,obj.b,obj.c,obj.d,obj.e)  # Inherited from Class1, Class2, Class3, Class4, and Class5

print(obj.method1())  # Inherited from Class1
print(obj.method2())  # Inherited from Class2





















