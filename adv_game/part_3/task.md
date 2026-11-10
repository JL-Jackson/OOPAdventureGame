#
# Moving between rooms

Finally, you should add a method to allow the player to move between rooms.

![img.png](house_img.png)

1. Go to the room.py file.
2. Add a move method to your Room class.
   The move method should have a parameter for the direction in which the player would like to move. If the direction
   is one of the directions linked to, the method returns the room object that is in that direction. If there is no room
   in the dictionary in that direction, the method returns self; that is, the player is linked back to the room they
   were already in.

       def move(self, direction): 
           if direction in self.linked_rooms: 
               return self.linked_rooms[direction] 
           else: 
               print("You can't go that way") 
               return self 

3. Go back to main.py and remove any code still left from your testing of the get_details() method.

       ballroom = Room("ballroom") 
       ballroom.set_description("A vast room with a shiny wooden floor; huge candlesticks guard the entrance") 
    
       kitchen.link_room(dining_hall, "south") 
       dining_hall.link_room(kitchen, "north") 
       dining_hall.link_room(ballroom, "west") 
       ballroom.link_room(dining_hall, "east") 

   any calls to get_details can now be removed

       kitchen.get_details() # remove 
       dining_hall.get_details() # remove 
       ballroom.get_details() # remove 

       #Add your code here 

4. Add some code at the bottom of the script to create a loop, letting the player move between rooms.

       current_room = kitchen           
    
       while True:		 
           print("\n")          
           current_room.get_details()          
           command = input("> ")     
           current_room = current_room.move(command)   

5. Save and run your program.

6. Type in some directions (e.g. “south”) to move between rooms.
   Don’t forget to also try directions that won’t work, to see whether your game handles them correctly.

   ### Moving between rooms
   
   Finally, you should add a method to allow the player to move between rooms.

7. Go to the room.py file.

8. Add a move method to your Room class.
   The move method should have a parameter for the direction in which the player would like to move. If the direction is
   one of the directions linked to, the method returns the room object that is in that direction. If there is no room in
   the dictionary in that direction, the method returns self; that is, the player is linked back to the room they were
   already in.

       def move(self, direction): 
           if direction in self.linked_rooms: 
               return self.linked_rooms[direction] 
           else: 
               print("You can't go that way") 
               return self 

9. Go back to main.py and remove any code still left from your testing of the get_details() method.

       ballroom = Room("ballroom") 
       ballroom.set_description("A vast room with a shiny wooden floor; huge candlesticks guard the entrance") 
    
       kitchen.link_room(dining_hall, "south") 
       dining_hall.link_room(kitchen, "north") 
       dining_hall.link_room(ballroom, "west") 
       ballroom.link_room(dining_hall, "east") 
    
       #any calls to get_details can now be removed 
       kitchen.get_details() # remove 
       dining_hall.get_details() # remove 
       ballroom.get_details() # remove 
    
       #Add your code here 

10. Add some code at the bottom of the script to create a loop, letting the player move between rooms.

        current_room = kitchen           
     
        while True:		 
            print("\n")          
            current_room.get_details()          
            command = input("> ")     
            current_room = current_room.move(command)   

11. Save and run your program.

12. Type in some directions (e.g. “south”) to move between rooms.
    Don’t forget to also try directions that won’t work, to see whether your game handles them correctly.

## Checklist

At the end of this lesson you should have:

- [ ] a method to move from room to room called `move()`
- [ ] the ability to move between rooms without errors if the direction isvalid or not
