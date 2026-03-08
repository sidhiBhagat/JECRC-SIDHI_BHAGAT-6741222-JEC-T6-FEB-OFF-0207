class Temp:
    def sum(self, a, b):
        return a + b
    #Monkey patching: Process of storing the prev method address inside avariable before overriding it with the new method address. Uisng the variable we can access the prev method.
    add_two_numbers = sum

    def sum(self, a, b, c):
        return a + b + c
    

t = Temp()
print(t.add_two_numbers(1, 2))     
print(t.sum(1, 2, 3))    


# AI driven quality engineering
# robo Python
# basics of performance Eng:selenium, web driver, browsersetup, locators, handling- form ,keyboards, touchpad, basic js and dom
# api automation