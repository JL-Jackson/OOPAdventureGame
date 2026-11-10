#

# Interacting with your game

At the moment, the only action your game allows you to take is to move between rooms, using the basic loop
you wrote at the end of part6:

	current_room = kitchen 
	 
	while True:		 
	    print("\n") 
	    current_room.get_details() 
        inhabitant = current_room.get_character()
        if inhabitant is not None:
            inhabitant.describe()
	    command = input("> ") 
	    current_room = current_room.move(command) 

Now that you have characters in some rooms, you need to expand this loop so that it performs different actions depending
on the command that is given. Here is some code to start you off:

	command = input("> ") 
	 
	# Check whether a direction was typed or other command
	if command in ["north", "south", "east", "west"]: 
	    current_room = current_room.move(command) 
	elif command == "talk": 
	    # Add code here 

Here are some tasks for you to complete.

### Task 1

Add some functionality to the game loop so that different commands can be recognized. For example, your program could
react to the following user inputs:

- ‘talk’: talk to the inhabitant of this room (if there is one). Return conversation text if present or other response
  if not.
- ‘fight’: ask what item the player would like to fight with, and then fight the inhabitant of this room
  (if there is one and if they are an enemy).

### Task 2

If you lose a fight with an enemy, the game should end.
Hint: The fight method you wrote in the Enemy class returns True if you survive and False if you do not.

### Task 3

Add a character to inhabit another room in your game. Perhaps you might want to add more methods in the Enemy
class in order to be able to interact with enemies in other ways. For example, can you steal from an enemy,
bribe an enemy, or send it to sleep?
**Tip:** To add a non-enemy character to your game you will need to import the Character class from the character
module, using:

	from character import Character 

**Note:** You can also import multiple things from the same module on the same line, like this:

    from character import Character, Enemy

### Task 4

For a bigger challenge, extend the Character class in a different way. You could create a Friend subclass
with some custom methods and attributes. For example, you could hug a friendly character, or offer them a
gift. You can use the built-in Python function [
`isinstance()`](https://docs.python.org/3.13/library/functions.html#isinstance)
to check whether an object is an instance of a particular class.

## Checklist

At the end of this lesson you should have:

- [ ] added functionality to the game loop so that different commands can be recognized
- [ ] more than one character in your game in separate rooms
- [ ] a fight method that ends the game if you lose
- [ ] multiple character types in your game, with different methods and attributes