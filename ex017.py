from sys import argv
from os.path import exists

script, from_file, to_file = argv

print("Copying from %s to %s" % (from_file, to_file))

# we could do these two on one line too, how?
# opens the file and we save the io stream
in_file = open(from_file)
indata = in_file.read(4)

print(type(in_file)) # _io.TextIOWrapper
print(type(indata)) # str

print("The input is %d bytes long" % len(indata))

print(("Does the output file exist? %r" % exists(to_file)))
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done.")

out_file.close()
in_file.close()