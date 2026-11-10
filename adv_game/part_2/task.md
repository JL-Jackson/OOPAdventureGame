#

# Classes & objects

In the previous step, you created a class called `Room` and a constructor method with attributes. You also instantiated
an object from the Room class. In this step, you are going to learn more about class and objects.
You can think of class as being a blueprint or a design of a house; it contains details about the make-up of the house
such as the doors, windows, floors, and roof.

When the design is built, a house is created; in this analogy, the built house is the object. You can build many houses
using the same design, likewise you can also create many objects from a class.

An object is also called an _instance_ of a class, and the process of creating this is _instantiation_.

In the main part of your game, the line below creates a new Room object with an attribute name set to kitchen. Then the
object is assigned to a variable called kitchen:

     kitchen = Room("kitchen") 

To fully understand how this works, you need to know how the `self` parameter works in the constructor. The `self`
parameter automatically receives a reference to the object invoking the method. By using self, a method can invoke
the object and access the attributes and methods of that object. In the previous constructor method, the parameter
`self`
automatically receives a reference to a new `Room` object while the parameter `name` receives `kitchen`. The line below
creates the attribute:

     self.name = room_name 

### Ballroom and dining room objects

Now you are going to create objects for the ballroom and dining room so that you have a total of three rooms in your
game.

1. Open your main.py file.
2. Add the following line of code to create a ballroom:

        ballroom = Room("ballroom")

3. Add another line similar to the one above of code to create a dining_hall room.

### Linking rooms

You now need to be able to locate these rooms in ‘space’ so we need to add another piece to the `__init__` area.

Considering that each adjacent room is going to have 2 pieces of information, it would be helpful to use a _dictionary_.

     self.linked_rooms = {}

As for the method description for linking the rooms in the class, we will need to gather those two pieces of
information:

- the name of the rome adjacent and
- the direction to which it is located.

       def link_room(self, room_to_link, direction):
           self.linked_rooms[direction] = room_to_link

### Using your new method

Use the link_room method you created to link the ballroom and dining hall to the kitchen.

Go back to your main.py file and add this line of code below the line where you instantiate the object:

     kitchen.link_room(dining_hall, 'south')

Did you notice that the method you wrote had three arguments (self, room_to_link and direction)? You do not need to ever
provide the self argument outside the class definition but the rest are necessary. Set the dining hall to the south
of the kitchen and the ballroom to the west of the dining hall. Clearly when you ‘place’ these rooms you will also have
to reciprocally place the other room.

**For example**: if the kitchen has the dining all to the south, the dining hall will
have the kitchen to the north. This will also need to be done.

You can also use the get_description method you will be creating next to include the liked rooms as a part of the
description.

Save and run your program.

## Task:

Your job is to create links to all the rooms in you main.py file.

### Getters and setters

So that you are able to interact with the room object, you need to create some _getters_ and _setters_. These are
methods
that get and set the values of the object’s attributes.

For every method within a class, you first need to specify the `self` parameter — the object itself — followed by any
data
to pass in, just as you did with the constructor. You will need to add these methods inside the room.py file, after the
constructor method.

    class Room():
        def __init__(self, room_name):
            self.name = room_name
            self.description= None

Here is a method to **set** the description of the room:

        def set_description(self, room_description):
            self.description = room_description

Here is a method to **get** the description of the room:

        def get_description(self):
            return self.description

### Using getters and setters

Use the set_description method you created earlier to give your kitchen object a description.

Go back to your main.py file and add this line of code below the line where you instantiate the object:

     kitchen.set_description("A dank and dirty room buzzing with flies")

Did you notice that the method you wrote had two arguments (`self` and `room_description`), but in the code above I only
had
to provide the room description? The self argument is always given first when you write a method, but when you use a
method, you do not have to give this argument to it. This is because it is automatically passed to the method when you
use Python.

You can also use the `get_description` method you created earlier. Add this line at the bottom of your main.py file:

     kitchen.get_description()

Save and run your program.

You will probably be expecting to see the description of your kitchen room on the screen. However, when you run the
program, you will not see anything. This is because your `get_description()` method returns the description, rather
than printing it. This is useful if you want to do something else with the description, such as concatenate it with
some other text, but if you want to display the description, you need to use the print command.

Instead of amending the `get_description()` method, you will use a different approach. Go back to room.py and add
a method called `describe()`, which will print out the object’s description when it is called.

        def describe(self):
            print(self.description)

In `main.py`, delete the `kitchen.get_description()` and add `kitchen.describe()` on the same line, then run it to see
the
description appear.

## Task:

Add a getter method called `get_name` and a setter method called `set_name` to your class, to allow someone to get and
set
the attribute name in the same way.

### Python properties
You don’t strictly need getters and setters in Python, because you can access the attributes of the object directly (for
example, you could just `print(kitchen.description)`. Including getters and setters in your class is good programming
etiquette, because they are useful tools for ensuring that people are using your code in the way you expect, and for
minimizing the risk of unexpected errors.

Python also has a more advanced way of specifying getters and setters for attributes using the @property decorator.
While this is probably considered more pythonic, I have chosen not to cover this method until later in this course, to
keep things simple.

## Task:
Your job is to create a get and set method for the name of the object.

Displaying linked rooms
When entering a room in the game, the game displays a description of that room to the player, for example:

     The dining hall
     ------------------- 
     A large room with ornate golden decorations on every wall
     The kitchen is north
     The ballroom is west

Next, you will add a new method to the Room class to report the room name and description and the directions of all the
rooms connected to it.

Go back to the Room class and add a new method that will display all the rooms linked to the current room object. Don’t
forget to make sure the new method is indented, just like all the other methods.

         def get_details(self):
             for direction in self.linked_rooms:
                 room = self.linked_rooms[direction]
                 print( f"The {room.get_name()} is {direction}")

This method loops through the dictionary `self.linked_rooms` and, for every defined direction, prints out that direction
and the name of the room in that direction.

Go back to the `main.py` file and, at the bottom of your script, call this method on the dining hall object, then run
the
code to see the two rooms linked to the dining hall.

     dining_hall.get_details()

### Name and description

Add the code to the `get_details()` method so that it also prints out the name and description of the current room, as
in
the example above. Remember that you can refer to the current room as self inside the method.
Check that your `get_details()` method works for any room object by calling it on the kitchen and ballroom as well.

## Checklist

At the end of this lesson you should have:

- [ ] getters and setters for each attribute in the Room class
- [ ] a method to display the name and description of the current room and the directions of all the rooms linked to it
- [ ] a linked room method that links the kitchen to the dining hall and the dining hall to the ballroom
- [ ] 3 linked rooms and in the main.py file
