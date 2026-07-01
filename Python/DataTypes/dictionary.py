'''
    in dictionary order never matter
'''

my_details = dict(firstName = "Aryan", lastName = "Chaudhary" )
print(my_details);

print(my_details["firstName"])
del my_details["lastName"]

print(my_details);

print(f"all keys : {my_details.keys( )}")