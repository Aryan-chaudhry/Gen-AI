i = 1
while(i <= 10) :
    print(i, end = " ")
    i = i+1 # python dont have increment and decrement operator

fruits = ["apple", "mango", "banana", "grapes"]

for idx, fruit in enumerate(fruits, start=0):
    print(idx , " : ", fruit)