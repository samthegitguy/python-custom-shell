print("Initiating boot sequence")
print("Importing external data")
from sys import platform
if platform == "linux" or platform == "linux2":
	os = "linux"
elif platform == "win32" or platform == "win64":
	os = "windows"
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
    if os == "linux":
        cmd = commandnum(raw_input("Enter your command: "), knowncommands)
    elif os == "windows":
        cmd = commandnum(str(input("Enter your command: ")), knowncommands)
    if cmd == 0:
        print("Testing was successful")
    elif cmd == 1:
        exit = True
    elif cmd == 2:
	flips = input("How Many Flips?")
	listof = []
        while len(listof) - 1 < flips:
            flip = random.randint(1,2)
            if flip == 1: listof.append("Heads")
            elif flip == 2: listof.append("Tails")
            else: print("Somethings wrong, press CTRL + C")
        for y in listof:
            print(y)
print("Goodbye!")

