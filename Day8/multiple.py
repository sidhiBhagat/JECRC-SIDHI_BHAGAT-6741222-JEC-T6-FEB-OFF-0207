class Parent1:
    a=10

class Parent2:
    b=20

class Parent3:
    c=30    

class Parent4:
    d=40

class Child(Parent1, Parent2, Parent3, Parent4):
    pass

print(Child.a)  
print(Child.b) 
print(Child.c)
print(Child.d) 