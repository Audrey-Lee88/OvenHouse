| [Home](index.md) 	| [Project Evolution](ProjectEvolution.md)  | [Game Architecture](GameArchitecture.md) 	| [Results](Results.md)  | [About Us!](AboutUs.md)

## Game Architecture 

<p align="center"><img src="flowchart.png"/></p>
<p align="center">
  UML diagram of the main classes involved in the game
</p>

### Controls
The controls are located in the main script which allows the player to move using the arrow keys and interact with enemies and items. If the player runs into an enemy, the game ends, and it's Game Over. 

The Game class represents what the player sees and interacts with. The Levels class sets up the levels and each “item” in the levels for the player to see. The Sprite class is connected to all of the interactive sprites (Player, Minions, Witch, and Key) to establish the animations and updates for the sprites. The Minions class updates the minion's movements and collisions. The Witch class will include the code for the witch movement. The Player class is the sprite the player controls. The TileCache class takes the images and divides them into “tiles” to be put into the levels. The SortedUpdates class sorts the sprites by depth.


### Integrating Art

### Chasing Witch
The Witch class has a method that calculates the vectorizes the distance between the witch and the player, and then makes the witch follow the player depending on the set speed. Due to this method, the witch's speed is the only factor that can be modified and will be restricted; on the contrary, the witch's direction of movement will be free-form/unrestricted. 
<p align="center"><img src="witch_code.png" width="600"/></p>

