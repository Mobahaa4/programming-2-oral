"""

Liskov substitution : subclasses should be able to replace their parent class without
affecting the behavior of the program

"""

class Animal:
    def make_sound(self):
        pass


class Dog(Animal):
    def make_sound(self):
        return "Woof!"


class Cat(Animal):
    def make_sound(self):
        return "Meow!"
    
def Animal_sound(Animal):
    print(Animal.make_sound())
    
    
Animal_sound(Dog())
Animal_sound(Cat())

