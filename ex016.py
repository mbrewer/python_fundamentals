from sys import argv

script, filename = argv

# Telling user we're going to print out the provided file
print(("We're going to erase %r." % filename))
print(("If you don't want that, hit CTRL-C (^C)."))
print("If you do want that, hit RETURN.")

# Cues user to make choice 1 or 2
input("?")

# Open the file with write permissions
print("Opening the file...")
target = open(filename, 'w')

# Truncate (empty) the file
print("Truncating the file. Goodbye!")
target.truncate()

# Telling user we're asking for two lines
print("Now I'm going to ask you for three lines.")

# Save user input to 3 variables, line by line
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

# Telling user we're writing them to the file
print("I'm going to write these to the file.")

# Write saved input to the file, line by line => refactored
# target.write(line1)
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")

# Refactor using strings, formats and escapes to print out lines 1 - 3 with 1 target.write()
# file_lines = {line1, line2, line3}
new_file = target.write("%s\n%s\n%s" % (line1, line2, line3))

# Write a script similar to the last exerise that uses read and argv to read the file you just created
print(type(new_file))
script = open(new_file, 'a')
print("Are you reading this?")
print(script.read())
print("How about now?")

# Close the file
print("And finally, we close it.")
target.close()
