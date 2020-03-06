print("Initiating boot sequence")
print("Setting up command sequences")
knowncommands = ["test","exit"]
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
print("Goodbye!")

