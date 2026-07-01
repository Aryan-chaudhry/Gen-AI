# generators are function that can pause or resume their execution

def Names():
    yield "Aryan"
    yield "Ayush"
    yield "muskan"

name = Names();

print(Names())

print(next(name))
print(next(name))
print(next(name))