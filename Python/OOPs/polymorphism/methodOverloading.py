# by defualt python does not support method overloading
class calculate:
    def Add(self, *a):
        if(len(a) == 1):
            print (a[0])
        else:
            print(a[0] + a[1])
        

    
    
c = calculate()
c.Add(10)
c.Add(10,20)