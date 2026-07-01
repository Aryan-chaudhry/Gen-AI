def customer():
    print("Welcome ! what is your token no ? ")
    token = yield
    while True:
        print(f" Processing your info via token : #{token}")
        token = yield

info = customer()

next(info) # start point of generator

info.send("22BCS16750")