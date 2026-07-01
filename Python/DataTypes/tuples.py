books = ("hcverma", "ccharp") # tuple immutable

(book1, book2) = books # unpacking and store in variable 

print(book1, book2)

a,b = 2,3 # at the backend tuple is responsible to assign the value properly

print(a, b)

# membership testing

print(f"is datastructure is in books ? {'datastructure' in books}")
print(f"is ccharp is in books ? {'ccharp' in books}")