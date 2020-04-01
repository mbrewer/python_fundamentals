# will put 10 in place of d as part of assignment
x = "There are %d types of people." % 10

# assign string to var
binary = "binary"

# assign to string to var
do_not = "don't"

# will put the previously defined variables in place of the strings => they are arguments
y = "Those who know %s and those %s." % (binary, do_not)

print x
print y

print "I said: %r." % x
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e
