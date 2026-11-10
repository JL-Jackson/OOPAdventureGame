#

# Aggregation

## objects within objects

Now that you have written a class for creating an enemy, you are going to add Dave the zombie to your game. Open up the
program from last unit in which you began creating your game.

**Create an enemy in the room**

- Add the following line of code at the top of main.py to import your Enemy class.
  from character import Enemy

Remember that character is the name of the Python file from which you are importing, and Enemy is the name of the class
you are importing from it.

Below the code that links the rooms together, you need to recreate Dave.

	kitchen.link_room(dining_hall, "south") 
	dining_hall.link_room(kitchen, "north") 
	dining_hall.link_room(ballroom, "west") 
	ballroom.link_room(dining_hall, "east") 
	 
	# Write the code to create dave here 

Make sure you include some code to set Dave’s conversation and weakness attributes.

	dave = Enemy("Dave", "A smelly zombie") 
	dave.set_conversation("Brrlgrh... rgrhl... brains...") 
	dave.set_weakness("cheese") 

Next, situate Dave inside a room. To do this, you have to add a new parameter inside the Room class in room.py so that a
room object knows when it has a character inside it. Edit your Room class constructor to add a new field.

    class Room(): 
        def __init__(self, room_name): 
            self.name = room_name 
            self.description = None 
            self.linked_rooms = {} 
            # Add the character attribute here 
            
A room object now has a character attribute inside it, set to None. When set, the character attribute will store a
Character object. This ability to store one object inside another is called aggregation. In practice a room may be
empty, in which case this attribute will stay as None. The important thing is that a room now has the ability to contain
a character.

## Task

- Add set_character and get_character setter and getter methods to the Room class to enable putting a character inside a
  room.

### Putting Dave in a room

Using the set_character method you just created, put Dave into a room by adding this code to main.py, immediately below
the code where you created Dave:

	dining_hall.set_character(dave) 

You may be thinking, ‘Hang on a second, the room can contain a Character, but Dave is an Enemy!’ You are allowed to add
an Enemy instead of a Character because of polymorphism: an Enemy is a Character.

When you enter a room, if a character is present, the game should let you know.

In the main game loop, before you ask the user for a command, check whether there is an enemy in the room using your
getter method.

	while True: 
	    print("\n")          
	    current_room.get_details() 
	 
	    # Add your code here 
	 
	    command = input("> ")     
	    current_room = current_room.move(command) 

If there is an inhabitant in the room, use the describe method that was inherited by Enemy from the Character class to
show who is there.

        inhabitant = current_room.get_character() 
        if inhabitant is not None: 
            inhabitant.describe() 

Save and run your program. Move from the kitchen to the dining hall, and you should see the description of Dave the
zombie appear.

I choose to put the code to describe the inhabitant of a room in the main game code, but I could have put it in the
`get_details` method of the Room class or in the describe method. There is no right answer.

## Checklist

At the end of this lesson you should have:

- [ ] a character attribute in the Room class that can store a Character object
- [ ] an instantiation of the Enemy class in the main.py file including all setters called to set the attributes of the
  Enemy object
- [ ] a check somewhere in your code that will describe the inhabitant of a room if there is one
- [ ] an import that allows you to use the Enemy or Character class in the main.py file