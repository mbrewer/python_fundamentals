from sys import argv

# set up argv vars
script, input_file = argv

# define function that takes 1 arg (file obj) and prints out contents to screen after reading file
def print_all(f):
	print(f.read())

# define function that starts at the beginning of the file, byte 0
def rewind(f):
	f.seek(0)

# define function that checks total length of file in bytes
def how_long(f):
	print(f.peek())

def print_a_line(line_count, f):
	print(line_count, f.readline())

current_file = open(input_file, "rb") # current file is <class '_io.TextIOWrapper'> 

print("First, let's print the whole file:\n")
print_all(current_file)

print("Now, let's rewind, kind of like a tape.")
rewind(current_file)

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

print("What is the number representing the stream?")
how_long(current_file)
