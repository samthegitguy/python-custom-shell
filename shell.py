print("Initiating boot sequence")
print("Saving data")

knowncommands = ["test","exit"]
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
while exit != True:
    cmd = commandnum(raw_input("Enter your command: "), knowncommands)
    if cmd == 0:
        print("Testing was successful")
    elif cmd == 1:
        exit = True
print("Goodbye!")

