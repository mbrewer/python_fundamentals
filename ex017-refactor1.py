from sys import argv
from os.path import exists

script, from_file, to_file = argv

# # print("Copying from %s to %s" % (from_file, to_file))

# # we could do these two on one line too, how?
# # by invoking open on the from_file, we create a file object (io)
# in_file = open(from_file)
# # invoking read on the file object creates a string object
# indata = in_file.read()
# # indata1 = in_file.read(10)

# # print(type(in_file)) # <class '_io.TextIOWrapper'>
# # print(type(indata)) # <class 'str'>
# # print(type(indata1)) # <class 'str'>

# print("The input is %d bytes long" % len(indata))
# print(type(len(indata))) # <class 'int'>

# # print(("Does the output file exist? %r" % exists(to_file)))
# # print("Ready, hit RETURN to continue, CTRL-C to abort.")
# # input()

# out_file = open(to_file, 'w')
# out_file.write(indata)

# # print("Alright, all done.")

# out_file.close()
# in_file.close()

# ###

# in_file = open(from_file).read()
# out_file = open(to_file).read()

open(to_file).write(open(from_file).read())
