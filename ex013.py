from sys import argv

script, first, second, third = argv

# overwrite CLI args with user input

print("What is your name?")
script = input()
print("What is your age?")
first = input()
print("What is your business here?")
second = input()
print("Are you ready to leave?")
third = input()

print ("\n")
print ("The script is called:", script)
print ("Your first variable is:", first)
print ("Your second variable is:", second)
print ("Your third variable is:", third)
print ("Hi!", 4*4)

print (type(script))
print (type(first))
print (type(second))
print (type(third))

# How can you make argv and input() work together?