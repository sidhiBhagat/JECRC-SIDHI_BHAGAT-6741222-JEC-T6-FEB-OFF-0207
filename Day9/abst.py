from abc import ABC, abstractmethod

class ATM(ABC): ##Abstract class
    @abstractmethod
    def generate_pin(self):
        pass

    @abstractmethod
    def forget_pin(self):
        pass

    @abstractmethod
    def check_bal(self):
        pass

    @abstractmethod
    def deposit(self):
        pass

    @abstractmethod
    def withdraw(self):
        pass


class SBI_ATM(ATM): ##Concrete class
    def generate_pin(self):
        print('It is used to generate ATM pin.')

    def forget_pin(self):
        print('It is used to forget the pin.')

    def check_bal(self):
        print('No balance is their in the account.')

    def deposit(self):
        print('Save money by giving it to me.')   

    def withdraw(self):
        print('It is used to withdraw the money.')

obj = SBI_ATM()
obj.generate_pin()
obj.forget_pin()   
obj.check_bal()
obj.deposit()
obj.withdraw()