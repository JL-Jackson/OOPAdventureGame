#

# Types of attribute

There are different types of attributes: _public_, _protected_, and _private_ attributes.
During this course, you have created public attributes that are available outside the class.
Most programming languages support the following attribute access levels:

- Public: can be changed outside the class
- Protected: can only be changed by the class or a subclass
- Private: can only be changed by the class

Attributes within Python are always public, but there is a convention of using either no, single, or
double underscores before an attribute name to denote its access level. For example:

    class MyClass(): 
      def __init__(self): 
        # no underscore = public 
        self.my_attribute = None 
 
        # single underscore = protected 
        self._my_attribute = None 
 
        # double underscore = private 
        self.__my_attribute = None 

By describing the access level of an attribute, you are stating how it can be used.

## Class and instance variables

The attributes in a class are just variables used to store data within an object of that class. Each time
you create an object, that object has its own set of these variables.

So far, all the attributes you have created within the class have been what are known as instance variables.
For example, your Enemy class has this attribute:

        self.weakness 

This attribute stores the weakness of the enemy, represented by this instance of an enemy object.
It can be set to a different value for each enemy object. Even if you were to set the same weakness for
two different enemy objects, each object would have its own separate copy of the weakness. If you alter
the weakness attribute of one object, the weakness attribute of another object of the same class is unaffected.
You can create two enemy objects, for example Dave and Brian, and set the weakness attribute to be different
for each of them:

![img.png](dave_and_brian.png)

I like to imagine an instance variable like a notebook. My friend and I might each own the same notebook, with the same
cover, but these books are separate instances. If I draw in my notebook, the drawing does not also appear in my friend’s
copy of the notebook.
You may now be able to guess how a class variable is different from an instance variable. A class variable is like
having a shared notebook, with its contents available to all notebook owners, i.e. all objects of that class.
You can create a class variable in Python by adding it outside of the constructor.

	class MyClass: 
	 
	    # class variable outside the constructor 
	    my_class_variable = 0 
	 
	    def __init__(self): 
	        # instance variable inside the constructor 
	        self.my_instance_variable = None 

## Using class variables

You can use a class variable to keep track of the number of rooms you have in your game.
First, add a class variable to the `Room` class, outside the constructor.

	class Room: 
      number_of_rooms = 0 

To use a class variable you use the name of the class, as opposed to the name of an object, for example:

	Room.number_of_rooms = 1 

Each time a `Room` object is created, you can increment the `number_of_rooms` class variable in the
constructor to keep track of the rooms created.

	class Room
      number_of_rooms = 0
      def __init__(self, room_name): 
        ... 
        Room.number_of_rooms += 1 

Regardless of how many rooms are created, the total number will be available in the class variable
`Room.number_of_rooms`.

	kitchen = Room("kitchen") 
	ballroom = Room("ballroom") 
	dining_hall = Room("dining hall") 
	 
	print(f"There are {Room.number_of_rooms} rooms to explore.") 

How do you think class variables might be of use to you in creating your game?
Can you think of any other situations in which you would need a variable to be shared by all instances of a class?

## Checklist

At the end of this lesson you should have:

- [ ] a class variable in the `Room` class to keep track of the number of rooms created
- [ ] a constructor that increments the class variable each time a `Room` object is created
- [ ] a print statement that displays the total number of rooms created
- [ ] make a main block for this lesson for the 'check' to work correctly. To do this, place the game loop inside a main block.
 
