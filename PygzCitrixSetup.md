<!---
layout: page
title: "PyGame Zero Citrix Setup"
permalink: https://Carreiroa.github.io/PyStringFn/
--->

### [Home](/index.md) | [Scratch](/ScratchIndex.md) | [Java](/JavaIndex.md) | [Python] (/PythonIndex.md)


---
### PyGame Zero Citrix Setup
---

Before we can start to create or run any games that use PyGame Zero there is some setup that we will need to do. Follow these steps to install the necessary modules so that your games run.

Step 1
: Log on to Citrix on your classroom desktop and launch VSCode.

Step 2
: From the top menu bar select `Terminal` and then `New Terminal`
: You could also hold down \<ctrl> - \<shift> - < ` >
![Terminal](/images/pgzinstall1.png)
![New Terminal](/images/pgzinstall2.png)

Step 3
: A terminal window will be displayed at the bottom of the VSCode window.
: Before installing the modules we will need we will update Python's package manager called pip by typing the following into the command line: `python.exe -m pip install --upgrade pip`
![Upgrade pip](/images/pgzinstall3.png)

Step 4
: After it is done updating, we will install PyGame by typing `pip install pygame` into the command line.
![Install PyGame](/images/pgzinstall4.png)

Step 5
: Once that's finished, let's now install PyGame Zero. Type `pip install pgzero` into the command line.
![Install PyGame Zero](/images/pgzinstall5.png)

That's it! You have now installed all the modules necessary to get started on your first PyGame Zero project. Let's test it out with the code below:

```python
import pygame
import pgzero
import pgzrun

WIDTH = 800
HEIGHT = 600

box = Rect (20,20,100,100) # Place a rectangle at position 20,20 and make the rectangle 100 by 100

def draw():
    screen.clear()  # Clear the screen
    screen.draw.filled_rect(box,'red') # draw the box and make it red

def update():
    box.x += 2 # Move the box 2 pixels to the right each frame

pgzrun.go() # ends pygame zero

```