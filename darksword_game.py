import sys
import time

decide = "Press 1 for yes, or 1 for no"

def start():
	print "\nYou are at the moat at the bottom of the mountain."
	print "You must make your way to the top, fighting a host of foes,"
	print "where you will have to defeat Alexander, the fire Dragon." 

	print "Do you wish to continue the journey?\n"
	print(decide)
	input = raw_input("> ")
	if input == "1":
		leave_moat()
	else:
		die("Ah, come on.")

def leave_moat():
	print "Good idea."
	print "\nOk, we are now crossing the bridge", 
	task()
	print "\nNow we are walking up the mountain", 
	task()
	print "\n\nOh no! The goblin of the western hills has appeared!"
	print "Do you wish to fight or flee?"
	print(decide)
	input = raw_input("> ")
	if input == "1":
		fight_goblin()
	else:
		die("Ah, he's not that bad!")

def fight_goblin():
	print "Do you wish to hit him in the 'head', 'heart', or 'stomach'?"
	input = raw_input("> ")
	if "head" in input:
		print "You knocked him in the head! Hurry before he regains consciousness!"
		fight_ghost()
	elif "heart" in input:
		print "You punched him in the heart! Hurry before he regains consciousness!"
		fight_ghost()
	else:
		print "You punched him in the stomach! Hurry before he regains consciousness!"
		fight_ghost()

def fight_ghost():
	print "We are again heading high up the mountain"
	task()
	print "Oh no, here is the ghost of the hills! You can't just punch him. How"
	print "are you going to kill him?"
	print """
	Select the number:
		1) Call the Ghostbusters
		2) Burn it in fire
		3) Join him on the otherside
"""
	input = raw_input("> ")
	if input == "1":
		print "Alright, the Ghostbusters have taken care of the ghost! Onward!"
		fight_dragon()
	elif input == "2":
		print "You've burnt the ghost with fire!"
		fight_dragon()
	else:
		die("You died, game over.")

def fight_dragon():
	print "Ok, now you must fight the monster!"
	die("You won! Game over!")
	
			

#Kill the program
def die(reason):
	print reason, "Try again!"
	exit(0)

#Set getanswer function to variable for testing
def task():
	for i in range(5):
		time.sleep(1)
		sys.stdout.write(".")
		sys.stdout.flush()

start() 
