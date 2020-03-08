print("Initiating boot sequence")
print("Importing external data")
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
    cmd = commandnum(raw_input("Enter your command: "), knowncommands)
    if cmd == 0:
        print("Testing was successful")
    elif cmd == 1:
        exit = True
    elif cmd == 2:
        flips = input("How many coins would you like to flip?")
        y = 0
        while y > flips:
            flip = random.choice("H","T")
            if (flip == "H"):
                print("Heads")
            elif (flip == "T"):
                print("Tails")
            else:
                print("Something's wrong.")
            y = y + 1
            print("test")
print("Goodbye!")

