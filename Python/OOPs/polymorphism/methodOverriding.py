
class Animal:
    def Name(self):
        print("I am Animal")

class Dog(Animal):
    def Name(self):
        print("I am Dog")

d = Dog();
d.Name()