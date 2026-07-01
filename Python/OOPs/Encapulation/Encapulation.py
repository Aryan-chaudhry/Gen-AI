class Bank:
    def __init__(self, name, accountNo):
        self.name = name
        self.__accountNo = accountNo
    
    def Name(self):
        print(self.name)

    def Account(self):
        print(self.__accountNo)

pnb = Bank("Aryan", "22BCS16750")
# print(pnb.__accountNo) give error because it is private
pnb.Name()
pnb.Account()