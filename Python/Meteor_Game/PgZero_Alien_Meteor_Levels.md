<!---
layout: page
title: "Python String Functions"
permalink: https://Carreiroa.github.io/Python/Meteor_Game/PgZero_Alien_Metor_Levels/
--->

# Alien Meteor Game
### Adding levels to your game

It's fun floating around in space with your alien, collecting gems and dodging meteors, but it can get boring after a while. What good is a game if it doesn't have levels. A challenging game that gets harder as it goes on is a much better game! So let's level up our game.

To do that we will need to check in with our own learning and consider what we already know:

You should already know:

* What imports you need to make things work
* How to setup the basic shell of a PyGame Zero game
* What variables are predefined in PyGame zero
* How to create an Actor
* What parts of your actor return x and y coordinates
* What the draw() and update() definitions do
* Why we need to use the key word `global` with variables inside a function
* How to move your actors on the screen automatically and via the keyboard
* How to display text on the screen

If you are comfortable with all of those things then you're ready to move on. If you are not, then you absolutely need to go back and review the tutorials and ask questions. Let's continue but this time the tutorial will provide you with instructions on a concept to be applied and you will need to make adjustments to your code. There may be code snippets for you to copy out if needed, but for the most part you should be able to implement the changes without having to copy them.

# Step 1

Consider that up until now you have been coding one complete level and what really makes the level behave and display the way it does are the `draw()` and `update()` functions. So it stands to reason that we will need unique `draw()` and `update()` functions for each level we create.

Take a look at the following code:
```python

WIDTH = 800
HEIGHT = 600
level = 1

def draw():

    if level == 1:
        drawLevel1()

    if level == 2:
        drawLevel2()
       
    

def update():

    if level == 1:
        updateLevel1()
        
    if level == 2:
        updateLevel2()



########## Level 1 Functions ###########
def drawLevel1():
    pass
    # Code that draws level 1

def updateLevel1():
    pass
    # Code that updates level 1


########## Level 2 Functions ###########
def drawLevel2():
    pass
    # Code that draws level 2

def updateLevel2():
    pass
    # Code that updates level 2

   
pgzrun.go() # keeps the game window open until you close it
```
### Notes on the code
Notice how the code calls functions defined for each level. Pygame Zero always runs the `draw()` and `update()` functions in its game loop and within each of those functions the code calls other functions depending on the level that the player is on.
You may notice the `pass` key word. That was just used for this code. It tells the python interpreter that there is nothing to go over in the function and to pass it over. 

### What you need to do
Now that you have understand what is happening conceptually, you will need to apply it. Take your current `draw()` and `update()` functions


