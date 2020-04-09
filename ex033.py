
# set i's starting point at 0
# save the numbers in list datatype

def stop_before_then(x):
	i = 0
	numbers = []

	# while i is less than 6, do the following logic
	# logic is that while true, add a number incrementing by 1 until 5 is hit
	while i < x:
		print("At the top, i is %d" % i)
		numbers.append(i)
		print("")

	# this is the incrementer part of the loop 
		i = i + 1
		print("Numbers now: ", numbers)
		print("At the bottom, i is %d" % i)

	# print this string
	print("The numbers: ")

	# this is the instruction to iterate over the numbers list
	# we are just using this for loop to print out a nice list at the bottom
	for num in numbers:
		print(num)

stop_before_then(9)
stop_before_then(100)
stop_before_then(2)