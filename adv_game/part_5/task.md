#

# Adding new attributes and methods

![img.png](dave_fights.png)

At the moment, your Enemy class is functionally identical to the Character class, so it is a bit pointless. That’s why
you will start to add new functionality to customize it.

Add a new attribute to specify the weakness of the enemy character, so that you can defeat the character in-game.
An object of the class Character doesn’t have an attribute called weakness; this is a customization you are adding to
the Enemy class.

Each enemy will be vulnerable to an item that can be found in the game. For example, you could make an enemy character
called Superman, who would be vulnerable to kryptonite.
Eventually you will use the Item class you wrote last week to add items to the game, but for now you can just represent
an item as a string.

1. Inside your Enemy class, move to the line below the one calling the superclass constructor.

        class Enemy(Character): 
            def __init__(self, char_name, char_description): 
                super().__init__(char_name, char_description) 
                # Write your code here 

2. Set the value of the weakness attribute to be initialized as None.

                self.weakness = None 

3. Add getter and setter methods to Enemy so that you can add a weakness for an enemy.

## Fighting Dave

The Character class has a method called fight(). As you don’t want to fight with non-hostile characters, it simply
returns a message that the character ‘doesn’t want to fight with you’.

1. Inside the Enemy class, you will now add a new implementation of the fight method to allow you to fight an enemy.
   This will override the implementation of fight() provided inside Character. Enter your method like this:

          def fight(self, combat_item): 

   combat_item is a string containing the name of an item, for example “sword” or “banana”.

2. In the game, you want the player to win or lose a fight with a character. Create a new method to fight:

          def fight(self, combat_item): 
              if combat_item == self.weakness: 
                  print(f"You fend {self.name} off with the {combat_item}" ) 
                  return True 
              else: 
                  print(f"{self.name} crushes you, puny adventurer") 
                  return False 

   The combat_item is the item the player is going to fight the enemy with. If it is the enemy’s weakness, the method
   should print out a message saying that the player won the fight, and return True. Otherwise, it will print out a
   message saying that the player lost the fight, and return False.

3. In your character_test.py program, add a weakness for Dave by calling the setter method you just wrote:

       dave.set_weakness("cheese") 

   In my game, Dave is vulnerable to cheese, because he just loves to eat it!

4. Call the fight() method on Dave, choosing an object to fight with:

       print("What will you fight with?") 
       fight_with = input() 
       dave.fight(fight_with) 

5. Save and run your code.
   If you choose to fight Dave with a melon, you will see this outcome of the fight:

       Dave is here! 
       A smelly zombie 
         
       [Dave says]: What's up, dude? 
       What will you fight with? 
       melon 
       Dave crushes you, puny adventurer 

6. Run the code again, but this time enter ‘cheese’ as the item you will fight with:

       Dave is here! 
       A smelly zombie 
       [Dave says]: What's up, dude? 
       What will you fight with? 
       cheese 
       You fend Dave off with the cheese 

In this step, you have customized the Enemy class to behave differently to its superclass, Character.

## Checklist

At the end of this lesson you should have:

- [ ] a weakness attribute in the Enemy class
- [ ] getter and setter methods for the weakness attribute
- [ ] a fight method in the Enemy class that allows you to fight an enemy
