# function
''' syntax def functionname():
                body
'''

def Vote():
    print(f"I can vote ")

Vote()

# function with arguments

def Vote(age): # paramter
    if(age >= 18):
        print("you can vote")
    else:
        print("you can not vote")

Vote(17)  # Argument

# *argument

def Bank(name, accountNo, branch, ifscCode):
    print(f" Your bank detail is name : {name}, accountNo : {accountNo}, branch : {branch}, ifscCode : {ifscCode}")

Bank("Aryan", "16750", "PNB-KUNJ", "132001")

def Bank(*args):
    print(f" Your bank detail is name : {args[0]}, accountNo : {args[1]}, branch : {args[2]}, ifscCode : {args[3]}")

Bank("Aryan", "16750", "PNB-KUNJ", "132001")

# **args used when you pass  keyword argument(dictionary)

def Bank(name, acc, branch, code):
    print(f" Your bank detail is name : {name}, accountNo : {acc}, branch : {branch}, ifscCode : {code}")

Bank(name = "Aryan", acc = "16750", branch = "PNB-KUNJ", code = "132001")

def Bank(**args):
    print(f" Your bank detail is name : {args["name"]}, accountNo : {args["acc"]}, branch : {args["branch"]}, ifscCode : {args["code"]}")

Bank(name = "Aryan", acc = "16750", branch = "PNB-KUNJ", code = "132001")

# lambda function

# syntax lamda arguments : expression

greeting  = lambda message  : print("hello " ,message)

greeting("Aryan")

# write lamdba function two add two number

add = lambda no1, no2 : no1+no2;
print(add(2,3))

