age = int(input("Enter your age : "))

if(age < 18):
    raise ValueError("age must be greater than 18")
else:
    print("you can vote")