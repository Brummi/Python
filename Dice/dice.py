from random import *

names = (1:"Felix", 2:"Calvin", 3:"Michael")

print("Welcome to the Dice simulator")
print("#############################")
print("Please specify the lower border")
min = int(input("Lower: "))
print("Please specify the upper border")
max = int(input("Upper: "))

while True:
    cmd = input("Command: ")
    if cmd == "exit":
        exit()
    else:
        r = randrange(min, max)
        print("Dice: {}".format(names:r))
