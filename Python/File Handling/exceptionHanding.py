
no1 = int(input("Enter number1 : "))
no2 = int(input("Enter number2 : "))

try:
    print(no1/no2)
except ZeroDivisionError:
    print("Division Error")


age = int(input("Enter your age : "))

if(age < 18):
    raise ValueError("age must be greater than 18")
else:
    print("you can vote")
    