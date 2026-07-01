'''
    list are mutable, it like an array
'''

data = ["water", "milk", "tea"]
data.append("sugar") # add

print(data)

data.remove("water")
print(data)


component = ["cup", "glass"]

component.extend(data);
print(component)

# add at specific index

component.insert(2, "plate")
print(component)

arr = [1]*3; # operator overloading
print(arr);

# connvert string into list

raw_list = bytearray(b"Aryan")

print(raw_list)




