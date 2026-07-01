'''
The key function for working with files in Python is the open() function.

The open() function takes two parameters; filename, and mode.

There are four different methods (modes) for opening a file:

"r" - Read - Default value. Opens a file for reading, error if the file does not exist

"a" - Append - Opens a file for appending, creates the file if it does not exist

"w" - Write - Opens a file for writing, creates the file if it does not exist

"x" - Create - Creates the specified file, returns an error if the file exists

In addition you can specify if the file should be handled as binary or text mode

"t" - Text - Default value. Text mode

"b" - Binary - Binary mode (e.g. images)

To delete a file, you must import the OS module, and run its os.remove() function:

'''

# creating file in python

file = open("readme.txt", "x")

# write text to a file

with open("readme.txt", "w") as f:
    f.write("Hello! i am readme.txt")

with open("readme.txt", "a") as f:
    f.write("\n i hope you are fine")

# open this file

file = open("readme.txt")
print(file.read())

import os

if(os.path.exists("readme.txt")):
    os.remove("readme.txt")
    print("file deleted successfully")
else:
    print("file with this name not found")