###############################################
#
# Author:       A. Carreiro   Date: 03/28/2023
#
# Module:       Inputbox
# Version:      1
#
# Description:  The following code is meant to 
#               be imported into a pygame zero
#               project and used as a text box.
#               When the enter key is pressed,
#               the value entered into the box is
#               returned.
#
# Issues:       Text box does not resize.
#               Text box does not take arguments
#               for colour or location.
#
# Usage:        Inputbox.py - must be in the same
#               directory as main py program.
#               import Inputbox
#               Inputbox.inputBox(screen.surface)
#
###############################################
     
import pygame
userInput =""


def input_to_string():
    pygame.event.clear()
    event = pygame.event.wait()
    
    if event.type == pygame.KEYDOWN:

        # manage key
        if event.key == pygame.K_BACKSPACE or event.key == pygame.K_RETURN:
             #userInput += " "
             return event.key
        else:
            return event.unicode

    else: # if the event is not key down.
        return None 


def inputBox(surface):
    global userInput # this will hold the text as it is populated
    # variables for the box
    boxColor = ("pink")#(224,224,224)
    topLeft = (20,20)
    botRight = (200,40)
    
    # create the box and draw it
    box = pygame.Rect(topLeft,botRight)
    pygame.draw.rect(surface,boxColor,box) #box filled
    pygame.draw.rect(surface,"green",box,1) #box outline

    # populate the box with text from userInput
    font =  pygame.font.Font(None,32)
    input_text= font.render(userInput,True,"white")
    surface.blit(input_text,(box.x+5,box.x+5))

    # set character to input from the keyboard
    character = input_to_string()
    
    # manage userInput
    if character != None:
        if character == pygame.K_BACKSPACE:
            userInput = userInput[:-1]
            return None
        elif character == pygame.K_RETURN:
            value = userInput
            userInput=""
            return value
        else:
            userInput += character # method
            return None