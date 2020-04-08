from sys import argv

script, name, age, weight = argv

print("This script is called %s" % script)
print("Your name is %s" % name)
print("You are %d years ago" % int(age))
print("You weigh %d pounds" % int(weight))
