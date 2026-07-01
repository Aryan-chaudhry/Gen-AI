class Employee:

    def setName(self, name):
        self.name = name

    def getName(self):
        print(self.name)
    

emp = Employee();

emp.setName("Aryan")
emp.getName();
