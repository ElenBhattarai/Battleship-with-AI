# **EECS 448 Project 2**
We recieved our project from Group 11 at the original repo [Here](https://gitlab.ku.edu/448-group-11/project-1).
We then converted it to a Github repo.

### [Agile Methodology](Agile.md)
^Click here to view information about our usage of the agile methodology.

### [Our Timesheet](Timesheet.md)
^Click here to view information about our timesheet.

Group Members:
- Elen Bhattarai
- Javante Ewing
- Alex Manley
- Max Dick
- Joaquin Vargas

# **Our Implementation**

## **The Software Architecture**

The project we inherited is implemeted in python `(version 3.10.0)` using a few external libraries. One of the libraries that is used is called Tkinter. The Tkinter library enables the use of frames to break the program into pieces that are linked together by frame activations. In this code, instead of the program running sequentially (ie. `Line 1`, `Line2`, `Line 3`) code is only run when it’s frame is activated. For this reason, the software architecture we inherited is an **`Event driven software architecture`**. For example, in their implementation one frame could be setting up the boards which then activates the next frame to allow players to place their ships. An advantage of this software architecture is twofold; one: it allows for simple debugging because if a frame has problems you already know where the bug exists in the code and two: it is simple to add new features as you just have to modify or add a frame to the order in which they are run.

#### [Inherited Documentation](Old.md)

## **Libraries Used**

- [Tkinter](https://docs.python.org/3/library/tkinter.html)
    >Enables the use of GUI and frame based programming.
- [functools](https://docs.python.org/3/library/functools.html)
    >Enables the use of partial functions on Tkinter buttons.
- [itertools](https://docs.python.org/3/library/itertools.html)
    >Enables simpler implementation of double in loops.
- [PIL/Pillow](https://pillow.readthedocs.io/en/stable/)
    >Enables image integration.
- [pygame](https://pygame.readthedocs.io/en/latest/1_intro/intro.html)
    >Enables in game sound effects.

## **File Structure**

- start.py
    >Handles program GUI.
- player.py
    >Stores player information like name and ships.
- ship.py
    >Stores ship information like placement and hit or miss.
- place_board.py
    >Handles ship placement logic.
- AI.py
    >Handles implementaion of player vs. computer gamemodes.

## **New Features**

For project 2, we implemented a few new features to the inherited game of Battleship.

### **AI Gamemode**

Using this new feature, the player can now play against the computer.

The AI gamemode has three different difficulties:
- Easy mode
    >The AI fires randomly each turn, regardless of a hit or miss.
- Medium mode
    >The AI fires randomly, but if it hits, then it attacks adjacent squares until a ship is sunk. 
- Hard mode
    >The AI knows where your ships are located and hits every turn.

### **Custom Features**

We then were tasked with implementing new custom features of our own choice.

- Big Shot Modifier
    >Enables an attack that hits a `(3x3)` area of shots.
    
    >Players are given 2 of these to use.
- Sound Effects
    >Enables sound effects during gameplay.

