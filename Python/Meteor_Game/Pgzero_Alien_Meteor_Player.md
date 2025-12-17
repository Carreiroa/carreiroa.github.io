---
layout: page
title: "Meteor Setup"
---
# Alien and Meteor Game

### Adding a player and game metrics

# Step 1

Now that we have our game with the meteor all setup it's time to add a player that we can move on the screen. For that we will use the pink alien in your images directory.

![Pink Alien](images\pinkalien.png)

Let's add them to our game window and place him  in the bottom left corner.

```python
####### Pink Alien #########
alien = Actor ('pinkalien')
alien.pos = 0,600



# This functions takes care of drawing images on the sceen
def draw():
    
    # Draw your actors on the screen. They appear in the order that 
    # you code them. This means that one image can overlap another.
    # Also, know that your actors are all rectangle objects.
    background.draw()
    meteor1.draw()
    alien.draw()
```
### Notes on the code
You will notice that your alien does not fully appear on the screen. 
![](images\step_1_image_1.png)

***The Fix***
```python
####### Pink Alien #########
alien = Actor ('pinkalien')
alien.pos = 0 + alien.width / 2 ,600 - alien.height / 2
```
### Notes on the code
You will notice now that your alien will fully appear at the bottom left corner. Take a look at the math that is applied to the position. Since alien.pos references the center of our object its necessary to change it by half its width and height for it to be displayed completely on the screen.
![](images/step_1_image_2.png)

# Step 2

Now that we have a player character, it's time to get them moving using the arrow keys. What we are looking to do is have our program listen for key inputs and if the correct keys are pressed the we alter the sprite's x or y coordinates.

```python
def update():
    # declaring that we are using the following global variables
    global m1_dx, m1_dy
    
    # move the meteor's location by the direction amount
    meteor1.x += m1_dx
    meteor1.y += m1_dy
    
    # detect edge of screen and reverse direction
    if meteor1.x <0 or meteor1.x > WIDTH:
        m1_dx = m1_dx * -1
    
    if meteor1.y <0 or meteor1.y > HEIGHT:
        m1_dy = m1_dy * -1
    
    ####### Alien Movement ######
    if keyboard.up:
        alien.y -= 1
        
    if keyboard.down:
        alien.y += 1
        
    if keyboard.right:
        alien.x += 1
        
    if keyboard.left:
        alien.x -= 1
```

# Step 3
Now that we can float our alien across space we will need to ensure that they don't float off the edges of our little universe. To do this we are going to handle its position within the if statements of its movement in the same manner we handled the meteor's bouncing off the edges of the window.

```python
 ####### Alien Movement ######
    if keyboard.up:
        alien.y -= 1
        if alien.top < 0:
            alien.y +=1
        
    if keyboard.down:
        alien.y += 1
        if alien.bottom > HEIGHT:
            alien.y -= 1
        
    if keyboard.right:
        alien.x += 1
        if alien.right > WIDTH:
            alien.x -=1
        
    if keyboard.left:
        alien.x -= 1
        if alien.left < 0:
            alien.x += 1
```

### Notes on the code
Take note of the nested ifs placed inside each condition. If the alien reaches the edge of the screen the code ensures that it undoes the incrementation or decrementation of the x or y variable.

# Step 4
Let's now manage a collision with the meteor. Now, we don't want to get hit by one, that would hurt. But if we do, that will cost us a life and we'll need to respawn in the bottom corner. We need to consider all that we will need to do in order to make this happen. We will need to manage the collision with `alien.colliderect(meteor1)` which will return true if it detects a collision, a variable that will keep track of our life count and some text on the screen to show us how many lives we have.

***Manage the collision***
```python
if keyboard.left:
        alien.x -= 1
        if alien.left < 0:
            alien.x += 1
            
####### Alien Collision #########      
if alien.colliderect(meteor1):
    alien.pos = 0 + alien.width / 2, 600 - alien.height / 2
```        
***Add life count variable***
```python
# set up the size of your window. Pgzero needs these variables to be
# named in all capital letters.
WIDTH = 800
HEIGHT = 600

speed = 2
life_count = 3
```
***Manage life count variable***
```python
def update():
    # declaring that we are using the following global variables
    global m1_dx, m1_dy, life_count
    
    """ Code removed for space saving reasons in this snippet """
            
    ####### Alien Collision #########      
    if alien.colliderect(meteor1):
        alien.pos = 0 + alien.width / 2, 600 - alien.height / 2
        life_count -=1
```

***Display your life count***
```python
def draw():
    
    # Draw your actors on the screen. They appear in the order that 
    # you code them. This means that one image can overlap another.
    # Also, know that your actors are all rectangle objects.
    background.draw()
    screen.draw.text(f"Lives left: {life_count}", (0, 0), color="yellow", fontsize=30)
    meteor1.draw()
    alien.draw()
```

### Notes on code
Your alien sprite is a rectangle and because of that we can detect collisions with other objects or rectangles by calling the function `alien.colliedrect(**Other rectangle object**)`. This code has chosen to have the alien detect what it collides with, but you'll notice that it will only detect a collision with one object. We will need to deal with that a little later if we're going to add other meteors.
You will also notice how we displayed the text on the screen. We used the screen object and called `screen.draw.text ( **String to be displayed**, **Location**, **colour**, **fontsize**)`

# Step 5
We'll now add gem to the mix, because a space alien dodging meteors needs to have some sort of mission. We will have our alien collect a gem that will appear on the screen. When the alien collides with the gem it will add to a score and relocate to a random location on the screen.

All you need to know to complete this task has already been done. Can you code this section yourself? ***Try coding it yourself before scrolling down for the code.*** Remember, if you get it to work and it doesn't look like the code below, that's okay. There are many different ways to code the same outcome.

***Adding gem and necessary components***
(Entire code below)
```python
import pygame
import pgzero
import pgzrun
import random
import math

# set up the size of your window. Pgzero needs these variables to be
# named in all capital letters.
WIDTH = 800
HEIGHT = 600

speed = 2
life_count = 3
score = 0

# We will use the Actor class to create various 'Actors' that will
# be used as game sprites and images to be displayed.

####### Meteor 1 ##########
background = Actor('starbackground800x600')
meteor1 = Actor('meteorbrown')
meteor1.pos = 400,300
# Randomize the direction of the meteor
m1_dx = random.uniform(-1,1)
m1_dy = random.uniform(-1,1)

# normalize the direction
magnitude = math.sqrt(m1_dx**2 + m1_dy**2)
m1_dx = (m1_dx/ magnitude) * speed
m1_dy = (m1_dy / magnitude) * speed

####### Pink Alien #########
alien = Actor ('pinkalien')
alien.pos = 0 + alien.width / 2, 600 - alien.height / 2

####### Gem ########
gem = Actor ('yellowgem')
gem.pos = random.randint(0,800),random.randint(0,600)



# This functions takes care of drawing images on the sceen
def draw():
    
    # Draw your actors on the screen. They appear in the order that 
    # you code them. This means that one image can overlap another.
    # Also, know that your actors are all rectangle objects.
    background.draw()
    screen.draw.text(f"Lives left: {life_count}", (0, 0), color="yellow", fontsize=30)
    screen.draw.text (f"Score: {score}", (0,30), color = "yellow", fontsize=30)
    meteor1.draw()
    alien.draw()
    gem.draw()
    
    
# This function updates variables and sprites as actions happen
def update():
    # declaring that we are using the following global variables
    global m1_dx, m1_dy, life_count, score
    
    # move the meteor's location by the direction amount
    meteor1.x += m1_dx
    meteor1.y += m1_dy
    
    # detect edge of screen and reverse direction
    if meteor1.x <0 or meteor1.x > WIDTH:
        m1_dx = m1_dx * -1
    
    if meteor1.y <0 or meteor1.y > HEIGHT:
        m1_dy = m1_dy * -1
    
    ####### Alien Movement ######
    if keyboard.up:
        alien.y -= 1
        if alien.top < 0:
            alien.y +=1
        
    if keyboard.down:
        alien.y += 1
        if alien.bottom > HEIGHT:
            alien.y -= 1
        
    if keyboard.right:
        alien.x += 1
        if alien.right > WIDTH:
            alien.x -=1
        
    if keyboard.left:
        alien.x -= 1
        if alien.left < 0:
            alien.x += 1
            
    ####### Alien Collision #########      
    if alien.colliderect(meteor1):
        alien.pos = 0 + alien.width / 2, 600 - alien.height / 2
        life_count -=1
    
    ######## Gem Collision #########
    if gem.colliderect(alien):
        score += 1
        gem.pos = random.randint(0,800),random.randint(0,600)
        
        
    
    


pgzrun.go() # keeps the game window open until you close it
```
