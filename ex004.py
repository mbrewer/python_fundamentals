cars = 100 
space_in_a_car = 4
drivers = 30
passengers = 90
# this is 100 - 30
cars_not_driven = cars - drivers
# this is the variable drivers
cars_driven = drivers
# this is 30 * 4
carpool_capacity = cars_driven * space_in_a_car
# this is 90 / 30
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We have need to put about", average_passengers_per_car, "in each car."