class Parent:
    gold='2 kg'
    silver='10 kg'
    no_of_flats=12

class YoungChild(Parent):
    name='Rickon'

class OldChild(Parent):
    my_name='John' 

class Sister(Parent):
    sis_name='Sansa'

print(YoungChild.gold) 
print(OldChild.silver)  
print(Sister.no_of_flats)  