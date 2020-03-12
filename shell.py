print("Initiating boot sequence")
print("Importing external data")
from sys import platform
import os
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
    elif cmd == 2:
	flips = input("How Many Flips?")
	listof = []
        while len(listof) < flips:
            flip = random.randint(1,2)
            if flip == 1: listof.append("Heads")
            elif flip == 2: listof.append("Tails")
            else: print("Somethings wrong, press CTRL + C")
        text_file = open("results.txt", "w")
        for y in listof:
            text_file.write(y)
            text_file.write("\n")
        text_file.close()
        print("Your results have been saved in results.txt")
print("Goodbye!")

