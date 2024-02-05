class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def print_(self, message)   :
        return f"{self.name} {message}"
    def bark(self):
        print(self.print_("is barking"))
    def eat(self):
        print(f"{self.name} is eating")
class SpecialDog(Dog):
    def __init__(self, name, age, kind):
        super().__init__(name, age)
        self.kind = kind
        
    def hunt(self):
        print(f"{self.name} is hunting so good")     
sp1 = SpecialDog("jessi", 11, True)
sp1.eat()
sp1.bark()
sp1.hunt()
        
