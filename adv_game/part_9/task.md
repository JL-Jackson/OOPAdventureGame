#

# Different types of method

During this course you have been using methods to interact with instances (objects) of classes. These
methods are known as _instance_ methods. There are two other types of method available in Python: _static_
and _class_. In this step you will explore the different types of method and how they can be used.

When you define a method, the first parameter of the method is named self and refers to the object that
called the method, for example:

	class MyClass: 
      def instance_method(self): 
        print(self) 

To use a method you must first create an instance (object) of the class. For example:

	my_object = MyClass() 
	my_object.instance_method() 

Static and class methods are different to instance methods in that you don’t have to create an object of the
class before you can use them. Static and class methods belong to a class, whereas an instance methods
belongs to the object.

Static and class method are useful if you want to create a function that is the same for all objects within
a class.

Review the code below, which includes a static method and a class method in addition to an instance method.

	class MyClass(): 
      def instance_method(self): 
        print(self) 
	 
      @staticmethod 
      def static_method(): 
        print("nothing") 
   
      @classmethod 
      def class_method(cls): 
        print(cls) 
	 
	my_object = MyClass() 
	my_object.instance_method() 
	MyClass.static_method() 
	MyClass.class_method() 

This code demonstrates that:

1. An instance method is passed self, a static method is passed nothing, and a class method is passed cls,
   which is the class the method belongs to.

2. To define a method as static or class, you use either the @static method or @class method decorator.

3. You call a static or class method via the class (MyClass.staticmethod()), not its object.

In the next step you will use instance, static, and class methods to create a class to describe your
role-playing game.

What scenarios can you think of for using static or class methods in your game?

## Welcome to the game

At the moment your role-playing game doesn’t welcome players to the game, or display how it was created and
by whom.

In this step you will create a new class to introduce the game, show how it was created, and display the
end credits. The information about how it was created and the method to show the credits should never change.

![img.png](img.png)

You can create this class by using a combination of instance , static, and class variables.

1. Create a new file called rpgInfo.py containing a new RPGInfo class with a single method that welcomes you to the
   game.

       class RPGInfo(): 
         def __init__(self, game_title): 
           self.title = game_title 
         
         def welcome(self): 
           print("Welcome to " + self.title) 

2. Import the `RPGInfo` class into your main program.

       from rpgInfo import RPGInfo 

3. Instantiate an object for your game and give the game a name, such as:

       spooky_castle = RPGInfo("The Spooky Castle") 
       spooky_castle.welcome() 

   Add info about how the game was made

   You should display some information about how the game was created using your RPG game generator. As the game created
   should always display the same message you can use a static class.

4. Add a static method called info to your RPGInfo class and add a suitable message.

       class RPGInfo(): 
         @staticmethod 
         def info(): 
           print("Made using the OOP principles") 

5. Call this static method from your main program using the name of the class.

       RPGInfo.info() 

## Adding credits

You should also provide a method that will show credits displaying at the end of a game, information about
who wrote the game.
While the information about your role-playing game generator should always be the same, different authors
should be able to use your classes to create games. However, the author will be the same for all games they
create, so it should be stored against the class, not the object.

6. Add a class variable to your class to store the author.

       class RPGInfo(): 
         author = "Anonymous" 

7. Create a class method that will output the credits and the author’s name.

          @classmethod 
          def credits(cls): 
            print("Thank you for playing") 
            print("Created by " + cls.author) 

8. Set the author’s name and call the credits class method at the end of your game.

       RPGInfo.author = "Jon Derpak" 
       RPGInfo.credits() 

Your complete `RPGInfo` class should look like this:

	class RPGInfo(): 
	    author = "Anonymous" 
	 
	    def __init__(self, game_title): 
	        self.title = game_title 
	 
	    def welcome(self): 
	        print(f"Welcome to {self.title}") 
	 
	    @staticmethod 
	    def info(): 
	        print("Made using the OOP RPG game creator (c) me") 
	 
	    @classmethod 
	    def credits(cls): 
	        print("Thank you for playing") 
	        print(f"Created by {cls.author}") 

Your main program should include the following code to use the RPGInfo class:

	from rpginfo import RPGInfo 
	 
	spooky_castle = RPGInfo("The Spooky Castle") 
	spooky_castle.welcome() 
	RPGInfo.info() 
	 
	RPGInfo.author = "Jon Derpak" 
	RPGInfo.credits() 

What other static or class methods could you add to the RPGInfo class?

## Checklist

At the end of this lesson you should have:

- [ ] an RPGInfo class with a welcome method that displays the game title
- [ ] static and class methods that display information about the game and the author 
