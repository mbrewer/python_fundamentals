print("You enter a dark room with two doors. Do you go through door #1 or door #2?")

door = input("> ")

if door == "1":
	print("There's a giant bear here eating a cheese cake. What do you do?")
	print("1. Take the cake.")
	print("2. Scream at the bear.")

	bear = input("> ")

	if bear == "1":
		print("The bear eats your face off. Good job!")
	elif bear == "2":
		print("The bear eats your legs off. Good job!")
	else:
		print("Well, doing %s is probably better. Bear runs away.") % bear

elif door == "2":
	print("You stare into the endless abyss at Cthulu's retina.")
	print("1. Blueberries.")
	print("2. Yellow jacket clothespins.")
	print("3. Understanding revolvers yelling melodies.")

	insanity = input("> ")

	if insanity == "1" or insanity == "2":
		print("Your body survives powered by a a mind of jello. Good job!")
	else:
		print("The insanity rots your eyes into a pool of muck. Good job!")

else:
	print("You realize that the doors were false choices and you keep going down the tunnel. \nCongrats on being woke!")
	print("It's so dark in here. Which one of these do you have in your pocket?")
	print("1. A match.")
	print("2. A candle.")
	print("3. An oil lantern.")

	cool_item = input("> ")

	if cool_item == "2" or cool_item == "3":
		print("You don't have a match! Damnit. You trip and plummet off a tunnel cliff. Goodbye!")
	else:
		print("Great! You've got a match. Now keep it lit.")
