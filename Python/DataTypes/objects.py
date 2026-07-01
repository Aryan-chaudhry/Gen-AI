'''
    every thing in python is an object it have 3 thing
    identity
    type
    value

    it may be mutable(changeable) or immutable(not changeable)
    we always validate with help of identity not by value

'''

# numbers are immutable 

sugar_amount = 3
print(f"Initial sugar : {sugar_amount}")


sugar_amount = 12 # we have changes the reference here so output is 12 but 2 is immutable because 2 is already ther so what is the proof of this yes --> check identity
print(f"Initial sugar : {sugar_amount}")

print(f"Id of 2 {id(2)}")
print(f"Id of 12 {id(12)}")


spice_mix = set(); # mutable
print(f"Initial spice_mix id : {id(spice_mix)}")

spice_mix.add("Ginger");
print(f"Initial spice_mix id : {id(spice_mix)}")
