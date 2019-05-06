| [Home](index.md) 	| [Project Evolution](ProjectEvolution.md)  | [Game Architecture](GameArchitecture.md) 	| [About Us!](AboutUs.md)

## Idea Evolution
OvenHouse had humble beginnings, we had no idea which direction we wanted to go with our final project. After our first conversation, we knew we wanted to build some an enjoyable game. Over the next two meetings, we decided to move forward with a classic fable, and specifically, Hansel & Gretel. 

Other Leading Ideas
The Boy Who Cried Wolf: You are the boy going around a dark village looking for villagers while avoiding the wolf
Save the Titanic: You are trying to get to the captain's control room
Pandoras Box: You decide not to open box, you win, if you open the box you need to solve puzzles

At this point, week three, we split up tasks and stuck with them for the duration of the project. Caleb on the timer + project organization + video, Audrey on the controls + backend + movement + collision, HK on the witch + text generation + key generation, and Kristtiya on custom artwork. The only non-artwork, and non-code pivot was with the video. The video began as a segmented short with each team member walking users through their contribution. It ended up being a fluid full gameplay with each player pointing out what they worked on and talking listeners through their process.

## Code Evolution
Our project also went through a few program iterations due to the nature of the main program.

In the beginning of the project, we were unsure how the graphics were going to look and how everything would interact with each other. Because of this, we wanted the code to be easily adaptable and integratable. Every person on the team was responsible for their respective tasks and making sure that the code they produced was adaptable. 

There were several executions to try and solve the “witch chasing” part of the code. HK took the lead on this end and tried to think of different ways to have the witch chase the player. First she was able to have the witch chase the player in the x-axis. Then, it evolved to having the witch chase the player based on the player’s and the witch’s coordinates and distance from each other. This method allowed the witch to move diagonally. We thought that this method would be the mechanism for the final game. However, when we integrated the “witch chasing” code into the main program, several issues arose. With the room-making algorithm, every sprite, object, and floor was initialized at the start and has to move according to the confines defined by the algorithm. This means that the witch could not move diagonally to chase the player. Audrey and HK worked together to remedy this by having the witch chase the player by moving either in the x or y direction depending on the player’s x and y relative position to the witch. This method is similar to the diagonal movement method, but instead, the witch can only move up, down, left, or right.

The minion movement was another mechanism that evolved in this project. Originally, we wanted the minion movement to be unpredictable and randomly change whenever they hit a wall. However, when testing this, we noticed that the minions would eventually just walk around the outside wall of the game or get stuck in between walls. This would make the game too easy for the player, so we decided to approach the minion movement differently. We decided to randomly assign minions a starting direction (up, down, left, or right), and when they collide with a wall, they would switch to the opposite direction (up -> down, left -> right, etc). This method proved to be effective since the minions’ paths were different each playthrough and still posed to be challenge to the player.

The placement of “keys” also evolved over the course of this project. Initially, we wanted the keys to be randomly generated in the level, so the player would have a different experience each time as they hunted down the keys. However, we decided that putting the keys in certain spots in the level would be more accessible code and visually wise.

## Artwork Evolution
Our project went through a few design iterations that varied due to the program, and also due to peer review.

Initially, the game was going to be in full color, with shading. The initial character was more bubbly, with round hands and a more oval face. We wanted her to have a sweeter look that shows innocence yet maturity so we redesigned her to look more proportional and with less vibrant colors.

We got mixed reviews for the character design, some liking and one deeply disliking. As a result the whole art style was redesigned in order to avoid further conflict. The current style is black and white, with some color standing out in order to represent significance in the story. 
Gretel for example now has no defined hair color or skin color in order to allow the player to become them. The main feature that stands out is her blue dress. The witch was also redesigned to seem more powerful, with an upper hand over the player. She is now floating on a cloud, which also ties into her ability to go over structures and through walls in her house. Her bright colors also present the power that she holds within herself. 
The rooms themselves also had a major redesign in order to fit with the room-making algorithm. Rather than being individual pngs, they features are all on bitmaps and have been redesigned and resized. 


### Gretel
<p align="center"><img src="gretel_dev.jpg" height = "300"/></p>
<p align="center">Gretel Development</p>

### Hansel
<p align="center"><img src="evolution/hansel.png" height = "300"/></p>

### Witch
<p align="center"><img src="evolution/witch_dev.png" height = "300"/></p>
<p align="center">Witch Development</p>

### Sprites
<p align="center"><img src="evolution/sprites.png" /></p>
<p align="center">Sprite Movements</p>

### Key
<p align="center"><img src="evolution/key_dev.png" height = "300"/></p>
<p align="center">Key Development</p>

### Layout
<p align="center"><img src="evolution/layout.png" width = "300"/></p>
<p align="center">Layout 1</p>
<p align="center"><img src="evolution/layout2.png" width = "300"/></p>
<p align="center">Layout 2</p>

### Others after redesign
<p align="center"><img src="evolution/furniture.png" width = "300"/></p>
<p align="center">Sample Furnitures</p>
