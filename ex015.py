from sys import argv

script, filename = argv

txt = open(filename)

print (("Here's the first line of your file %r:" % filename))
print (txt.readline())

# print ("Type the filename again:")
# file_again = input("> ")

# txt_again = open(file_again)

# print(txt_again.read())

script = open(filename)
print(script.read())
script.close()

# Good job! You did it.