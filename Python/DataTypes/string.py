'''
String are immutable

core
indexing
slicing [start : end(length) : step]

'''

firstName = "Aryan"
lastName = "Chaudhary"
fullName = firstName + " " + lastName # concatination

print("full Name : ", fullName);

print("name : ", fullName[0:8])

password = "Aryan齉"
Encoded_password = password.encode("utf-8")
print(f"Encoded password {Encoded_password}")

Decoded_password = Encoded_password.decode("utf-8")
print(f"Decoded password {Decoded_password}")