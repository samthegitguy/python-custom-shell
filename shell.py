print("Initiating boot sequence")
print("Preparing preboot required files")
text_file = open("results.txt", "w")
print("Importing external data")
from sys import platform
import os
import random
os.remove("results.txt")
if platform == "linux" or platform == "linux2":
	ops = "linux"
elif platform == "win32" or platform == "win64":
	ops = "windows"
import random
print("Setting up command sequences")
knowncommands = ["test","exit","coinflip"]
print("Writing functions")
def commandnum(enteredcommand, thelistofknowncommands):
    if enteredcommand in thelistofknowncommands:
        loop = True
        x = 0
        while loop == True:
            if enteredcommand == thelistofknowncommands[x]:
                loop = False
                return x
            else:
                x = x + 1
exit = False
print("Ready.")
while exit != True:
    if ops == "linux":
        cmd = commandnum(raw_input("Enter your command: "), knowncommands)
    elif ops == "windows":
        cmd = commandnum(str(input("Enter your command: ")), knowncommands)
    if cmd == 0:
        print("Testing was successful")
    elif cmd == 1:
        exit = True
    elif cmd == 2: from subprograms import coinflip
print("Goodbye!")

