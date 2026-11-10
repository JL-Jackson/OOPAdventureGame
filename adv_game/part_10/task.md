#

# Properties

A property is a special type of function that allows you to get and set attributes without the use of getter and setter
methods.

Many programming languages, including Python, support properties, although some languages, such as C++ and Java, do not.

As you have previously learnt, it is good practice to set attributes through the use of getter and setter methods, as
demonstrated in this class:

	class MyClass(): 
	    def __init__(self): 
	        self.my_attribute = 0 
	 
	    def get_my_attribute(self): 
	        return self.my_attribute 
	 
	    def set_my_attribute(self, value): 
	        self.my_attribute = value     
	 
	my_object = MyClass() 
	 
	my_object.set_my_attribute(1) 
	print(my_object.get_my_attribute()) 

As the attributes are public, it is possible in Python to access them directly using my_object. my_attribute, for
example:

	my_object = MyClass() 
	 
	my_object.my_attribute = 2 
	print(my_object.my_attribute) 

This approach would simplify the code, but with the downside that without wrapping the get and set into functions, you
cannot control how attributes in your class are updated. There would be nothing stopping someone setting the attribute
to an invalid value, for example:

	my_object.my_attribute = "some invalid value" 

Properties get around this problem by allowing you to define a function that is called when the value of an attribute
is changed directly.

I have modified the example class above to use a property instead of a getter and setter.

	class MyClass(): 
	    def __init__(self): 
	        self._my_attribute = 0 
	 
	    @property 
	    def my_attribute(self): 
	        return self._my_attribute 
	 
	    @my_attribute.setter 
	    def my_attribute(self, value): 
	        self._my_attribute = value 
	 
	my_object = MyClass() 

Walking through this code, you can see the following changes:

1. I have used an underscore ('_') to denote that the `my_attribute` attribute is protected. By doing so I am stating
   that this
   attribute should not be changed directly.
2. There are two new methods, both called `my_attribute`.
3. The `my_attribute` method that has the @property decorator before it is the getter and, when called, it will return
   the value stored in _my_attribute.
4. The second `my_attribute` method that has the `@my_attribute.setter` decorator is the setter. It accepts a single
   parameter which, when called, will set _my_attribute to the value passed.

To get the attribute you use the getter property method name, just as you would have for a normal attribute.

	the_value = my_object.my_attribute 

This calls the getter property method and returns the value of the object’s `_my_attribute` attribute.

	    @property 
	    def my_attribute(self): 
	        return self._my_attribute 

To set the attribute, you assign a value to the setter property.

	my_object.my_attribute = 3 

In the setter property, the value being assigned (3 in this case) will be passed as the value parameter:

	    @my_attribute.setter 
	    def my_attribute(self, value): 
	        self._my_attribute = value 

The advantage of properties is that you can maintain the simple syntax of object.attribute, but a function is being used
behind the scenes. This can be useful for tasks such as validation.
For example, you could modify the setter property to validate that the value being set is a positive number:

	    @my_attribute.setter 
	    def my_attribute(self, value): 
	        if value < 0: 
	            print("Invalid value") 
	        else: 
	            self._my_attribute = value 

Conversely, you could use the getter to modify the data before it was returned, for example by always returning the
attribute value as a string:

	    @property 
	    def my_attribute(self): 
	        string_attribute = str(self._my_attribute) 
	        return string_attribute 

## Task

Modify _one_ (or all) of the classes from your game to use properties rather than getter and setter methods.

## Finishing the game

Now it’s time to finish writing your game and put all the concepts you have learnt about into practice. Here are some
ideas for things you might want to do. I’ll show my example solutions in the next step so that you can see how I solved
these challenges.

### Challenge 1

Add the Item class you wrote in week two to your game. Follow the same process as for the Character class: add an
attribute to Room so that it can store an Item, and then create the Item and assign it to the Room. Inside the game
loop, check whether there is an Item in the room, and if so, describe it.

### Challenge 2

Add a backpack to allow the player to store items. This can be a list in the main part of the program, rather than a
separate class:

	backpack = [] 

When a player enters a room that contains an Item, the command ‘take’ should put the name of the current room’s Item
into the backpack, and also set the Item attribute of the Room to None.

### Challenge 3

Change your game so that when the player chooses an item to use in a fight, the game checks whether the player actually
has an item with that name in their backpack.

### Challenge 4

Use a class variable to allow the player to win the game only after they have defeated a specific number of enemies,
rather than winning it the instant they defeat a single enemy.

## Share your game

How did you go about completing the challenges? Was there anything you found difficult? Ask others to test and give
suggestions for your game.

## Handing in your work

To hand in your work, commit and push your changes to your GitHub repository.
