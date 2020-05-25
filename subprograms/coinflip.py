flips = input("How Many Flips?")
listof = []

if raw_input("An additional file (other than those downloaded at the beginning of this program) is required to use this program. Y/N: >  ").lower() != "y": exit()
import random
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
