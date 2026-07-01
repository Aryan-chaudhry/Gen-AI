# infine generators

def infinite_numbers():
    count = 1;
    while True:
        yield f"count #{count}"
        count += 1;

numbers = infinite_numbers();

for _ in range(3):
    print(next(numbers))