class Father:
    def Name(self):
        print("Abcd")

class Mother:
    def Name(self):
        print("Efgh")

class Child(Father, Mother):
    def Age(self):
        print(21)


Aryan = Child();
Aryan.Name()

