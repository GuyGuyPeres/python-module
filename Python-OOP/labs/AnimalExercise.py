class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def speak(self):
        return("An Animal Is Speaking...")
    
class Dog(Animal):
    def __init__(self, name, age, race):
        super().__init__(name, age)
        self.race = race
    
    def speak(self):
        return("Bark-Bark(DOG)")

dog1 = Dog("Rexi", "12", "labrador")    

print(dog1)
print(dog1.name, dog1.age, dog1.race)