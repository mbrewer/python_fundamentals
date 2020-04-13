from sys import exit

def gold_room():
	print("This room is full of gold. How much do you take?")

	next = input("> ")
	
	try:
		how_much = int(next)
	except ValueError:
		dead("You didn't steal quickly enough and the guards caught you!")

	if how_much <= 5000:
		print("Nice, you didn't take it all and anger the gods! You win.")
		exit(0)
	else:
		dead("You greedy goblin!")


def bear_room():
	print("There is a bear there.")
	print("The bear has a bunch of honey.")
	print("The fat bear is in front of another door.")
	print("How are you going to move the bear?")
	print("1. Take his honey")
	print("2. Taunt the bear")
	print("3. Open door")
	bear_moved = False

	while True:
		next = input("> ")

		if next == "1":
			dead("The bear looks at you then slaps your face off.")
		elif next == "2" and not bear_moved:
			print("The bear has moved from the door. Open it!")
			bear_moved = True
		elif next == "3" and bear_moved:
			gold_room()
		else:
			print("I got no idea what that means. Try again.")


def clhulhu_room():
	print("Here you see the great evil Cthulu.")
	print("He, it, whatever stares at you and you go insane.")
	print("Do you flee for your life or eat your head?")
	print("1. Flee")
	print("2. Stay")

	next = input("> ")

	if "1" in next:
		start()
	elif "2" in next:
		dead("Gross!!!")
	else:
		clthulu_room()


def dead(why):
	print(why, "Ya dead!")
	exit(0)

def start():
	print("You are in a dark room.")
	print("There is a door to your right and left.")
	print("Which one do you take?")

	next = input("> ")

	if next == "left":
		bear_room()
	elif next == "right":
		cthulhu_room()
	else:
		dead("You stumble around the room until you starve.")


start()