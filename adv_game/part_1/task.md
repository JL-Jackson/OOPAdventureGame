#

# Introduction

[Play this](https://iplayif.com/?story=https%3A%2F%2Fifarchive.org%2Fif-archive%2Fgames%2Fzcode%2Fzdungeon.z5)

This is what we want to emulate here. We want to create a text-based adventure game. In the process of making the game,
you will create objects, set attributes, and call methods. In the turtle race you started by using classes
that were already written so you have used and dealt with classes before but this will walk you through each step on how
to create your own.

You will:

- Create your own classes
- Learn how to use attributes and methods
- Create custom objects
- Use getter and setter methods

### Text Adventure Game

In this step, you will make a text-based adventure game and explore how you could use methods and attributes to
interact with a room in the game.

A text-based adventure game is an interactive-invented world described in text. It can be filled with different rooms,
items, obstacles, or anything your imagination allows. The player interacts with the world by typing commands, and the
game describes the result of the player’s commands.

You can move around the game by using the commands. For example: north, south, east, and west.
Each time you move, you enter a new room and a description is shown.
An example of a room in your game might be a dining hall, described like this:

    The dining hall 
    ------------------- 
    A large room with ornate golden decorations on every wall 
    The kitchen is north 
    The ballroom is west 
    > 

In the turtle_race, you looked at _attributes_ and _methods_.

Attributes are the pieces of information stored within an object, just like a collection of variables.

Methods are the ways in which you interact with an object; you used methods like `forward()` and `right()` to move the
turtle. In your adventure game, what methods do you think might be useful for interacting with a room?
As an example, you need to be able to display the name of a room when the player enters it, so you might write a
`get_room()` method. What _attributes_ do you think a room might have? For example, every room should have a name
(for example ‘kitchen’ or ‘dining hall’), so you will add an attribute called name.

Think about the attributes and methods that rooms might have.

### Creating your own class

In this step you are going to create your own class, which will be a blueprint for the rooms in your text-based
adventure game.

1. Start in the `room.py` file.
2. Create a class in that file and give it a name like this:

   `class Room:`

   Your class is called `Room` because it will represent the concept of a room. I have deliberately given the class a
   name starting with a capital letter, as this helps to distinguish between class names and variables. You'll notice
   that
   the IDE will automatically capitalize the first letter of the class name for you or give you a PEP8 warning if you
   don't.

   #### Creating a constructor and defining attributes

   You are now going to add a constructor to your class. This is a special method to tell Python how to create an
   object of this class, and it is always called __init__ with a double underscore on each side of ‘init’.
   Take extra care to get this special method name right, or your constructor will not work!

   Complete the following instructions in your `room.py` file:

3. Move to the next empty line.
4. If your editor has not done this for you, indent your cursor by pressing the tab key (pyCharm should do this) to tell
   Python that the code you are about to write is part of the Room class.
5. Add the code below to define the constructor method:

   `def __init__(self):`

   Here, ‘init’ stands for ‘initialize’, as a constructor initializes (that is, creates) an object.

   Now you are going to add attributes for your room to the constructor. The room should have a name — for example,
   it might be a kitchen, a bathroom, or a cellar. You are also going to store a description of the room to provide
   some atmosphere — the cellar could be dark and dusty, for instance.
   Add these attributes to your constructor method like this:

        def __init__(self): 
            self.name = None 
            self.description = None 

   Always refer to attributes within the object in the format `self.<name_of_attribute>` to tell Python that you are
   referring to a piece of data within the object; self means ‘this object’. Setting the attribute values to None means
   that they will start off with no value.

   Sometimes you will want to allow people to set the values of these parameters when they use your class to create an
   object.

   Add a parameter to the constructor called room_name by altering the existing code like this:

        def __init__(self, room_name): 

   This means that when you create an object, you must provide a room name.
   Change the code inside the constructor to tell Python to set the value of the attribute self.name to the room_name
   provided, by altering the existing code like this:

        def __init__(self, room_name): 
            self.name = room_name 

   Your `Room` class should now look like this:

        class Room(): 
            def __init__(self, room_name): 
                self.name = room_name 
                self.description = None 

   Instantiating your own object
6. Test your code out by creating an object of the Room class you have written.
   Now go to the file called `main.py` which is in the same folder as the file `room.py`.

7. In the `main.py` file, add the following line of code:

        from room import Room 

   This command looks for a file in the same folder called `room.py`, and looks inside that file for a class called
   `Room` (note the upper case R); this is the class you just wrote. The Room class is then made available for use
   inside the main.py file. (If you did not save your room code as room.py, this will not work; in this case, you will
   need to rename the file.)

   Now instantiate (create) a Room object by executing the code in your main.py file.
   ![img_2.png](kitchen.png)
   Add the following code in the next empty line in your main.py file:

        kitchen = Room("kitchen") 
   This stores the object in a variable called ‘kitchen’ so that you can refer to it later.

   When you save and run your program, nothing will happen. Your Room object is being created, but you can’t see it or
   interact with it, because you didn’t write any methods when you created the Room class. You will move onto this
   later.
   Your Room class has two attributes: a name and a description.

   Can you think of any other attributes a room in our
   game might have? Why do you think that attribute would be useful? 
