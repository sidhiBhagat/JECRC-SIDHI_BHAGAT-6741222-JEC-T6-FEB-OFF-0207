class Parent:
    bank_balance = '54lakhs'
    def __init__(self, *members):
        self.members = members

    def desc(self):
        print("I am the parent class")

class Child(Parent):
    def __init__(self, child_name, *args):
        self.child_name = child_name
        super().__init__(args)

c = Child('sidhi', 'vaibhav')
# print(c.bank_balance)  # Inherited class variable
print(c.members) 
print(c.child_name) # Inherited instance method