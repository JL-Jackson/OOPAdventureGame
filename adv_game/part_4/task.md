#

# Extending a class
Previously you used classes written by other people wrote your own class from scratch. We will now:

- Extend a class by adding your own functionality to existing code
- Look at the concepts of _inheritance_ and _polymorphism_
- Use inheritance and polymorphism in the context of your text-based adventure game to create enemies for the
  player to encounter

Extending a class takes advantage of a concept called inheritance; The new class can be said to inherit properties
from its parent class. To extend a class, you can define new attributes or methods, and you can also change the behavior
of existing methods.


![img.png](dave.png)
In this step you are going explore how to extend an existing class. It is also perfectly normal to write your
own classes and then extend them.

You will find a new file here called `character.py`. The code is a Character class that I have written for you.
If you have a look at it, you should recognize some familiar things.

You’ll see that to create a Character object, the constructor needs two parameters: the character’s name and a
description of the character:

	def __init__(self, char_name, char_description): 
	    self.name = char_name 
	    self.description = char_description 
	    self.conversation = None 

To test this create a new Python file and save it as character_test.py, in the folder with your other code. At the top
of this "test" file, import the Character class from the character.py file:

	from character import Character 
	dave = Character("Dave", "A smelly zombie") 

Add this code as well to call the describe method on the object you created to show the character’s description on
the screen.

	dave.describe() 

Save and run your program. You should see the description of the character you just created:

	Dave is here! 
	A smelly zombie 

### Tasks

1. Examine the Character class inside character.py to find the name of the method that sets the conversation attribute.
2. Add code to your test file to call this method and give Dave a line of dialogue.
3. Add code to your test file to call a different method that talks to Dave.

So far, so good. You can use this code as the basis for your characters. However, not every character in the game will
have the same characteristics. Some will be friends, and some will be enemies, and friend and enemies should behave
differently.

Your game will have multiple characters to interact with. For example, I might create two characters: Dave, the smelly
zombie, and Catrina, the friendly skeleton. I might want to fight with enemies such as Dave, but I wouldn’t want to
fight with friendly characters such as Catrina.

Inheritance is one of the key elements of OOP; it allows you to base a new class on an existing one. The new class
automatically inherits all the methods and attributes of the existing class, removing the need to include the same
methods and attributes in the new class.
You will make a subclass of Character called Enemy. It will use the Character class as a basis, but add some more
functionality specific to enemies.

### Tasks

In the existing character.py file, create a new Enemy class below the Character class.

	class Character(): 
	    ... 
	 
	    # Fight with this character 
	    def fight(self, combat_item): 
	        print(self.name + " doesn't want to fight with you") 
	        return True 
	 
	# Add your code here (first line unindented) 
	class Enemy(Character): 

The name of this new class is Enemy. Putting Character inside the brackets tells Python that the Enemy class will
inherit all the methods from Character.
Character is called the super class of Enemy, and Enemy is a subclass of Character.

Add code in the next line to create a constructor for an enemy object; this looks identical to the constructor of
Character.

    	def __init__(self, char_name, char_description): 

Character is the superclass of Enemy, so you need to ensure that Enemy inherits from Character. To do this, you have to
call the superclass constructor method inside the constructor of the Enemy class.

Add the code below, in the next line after the Enemy constructor.

			super().__init__(char_name, char_description) 

This line of code means ‘To make an Enemy, first make a Character object, and then I will customize it.’

When the `__init__()` function is created in a subclass, the subclass will no longer inherit the
superclasses' `__init__()` function.

The `super()` function allows you to call functions in the superclass.

Calling `super().__init__()` from the Enemy class will call the constructor of the Character superclass. The Character
constructor sets up the attributes for the class.

Calling the previously built methods with `super()` saves you from needing to rewrite those methods in your subclass.

Save this code. Next, you will prove that, with the help of these two lines of code, the Enemy class has inherited
all the properties of the Character class.

### Tasks

Go to your character_test.py program and change it so that all references to the Character class become references to
the Enemy class:

	from character import Enemy 
	 
	dave = Enemy("Dave", "A smelly zombie") 

Run the code and test it. You should be able to see the description of Dave and talk to him, just as you did before.

An object of a subclass is also considered to be an object of its superclass. In simple terms, a class that inherits
from a <superclass> is called a <subclass>.

So in your example, an Enemy is a Character.

If a function requires a Character object as a parameter, you can give the function an Enemy object instead and the
code will still work. However, this does not work the other way around: if the function requires an Enemy object, you
cannot give it a Character object, because Enemy is a more specialized version of Character.

In the next step, you will modify the Enemy class so that it behaves differently to the Character class. This concept
is called polymorphism.

How do you think an enemy object will behave differently to a character class in your game? What attributes might it
need? What methods might be useful?

## Checklist

At the end of this lesson you should have:

- [ ] a character.py file with a Character class and an Enemy class
- [ ] a test file that creates an Enemy object and tests it
