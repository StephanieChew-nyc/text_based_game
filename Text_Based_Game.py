#!/usr/bin/env python
# coding: utf-8

# In[3]:


import time

answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
yes = ["Y", "y", "yes"]
no = ["N", "n", "no"]

enter = 0
noentry = 0

required = ("\nUse only A, B, or C\n")


# In[2]:


def start():
    print("Welcome to the Adventure Game! Do you want to play? Y/N")
    choice = input(">>> ")
    if choice in yes:
        intro()


def intro():
    print ("You are a treasure hunter and searching for the rarest "
  "treasure to world. Miles away from the closest town, you found an "
  "abandon dungeon. However, you hear growling sounds coming from "
  "inside. Enter the dungeon? Y/N")
    choice = input(">>> ") #Here is your first choice.
    if choice in yes:
        print("You entered the dungeon.")
        option_yes()
    else:
        print ("\nYou give up your dreams for "
        "having a rich life. "
        "\n\nGame over!")

def option_yes():
    print ("Inside the dungeon is a high-ceiling "
  "room with a sleeping dragon. Behind the dragon "
  "is a door. What do you do?")
    time.sleep(1)
    print ("""  A. Throw a rock
  B. Run
  C. Sneak around it""")
    choice = input(">>> ")
    if choice in answer_A:
        print ("\nThe rock hit the dragon's head. It woke up. "
  "The dragon feels groggy, looks around the room and saw you. "
  "It ran to you, opened it mouth and ate you. \n\nYou died!")
    elif choice in answer_B:
        print ("\nYou ran away from the dragon and out of the "
  "dungeon. You never got the treasure. \n\nGame Over!")
    elif choice in answer_C:
        print ("You slowly sneak around the dragon. When "
    "you got to the door, you open it slowly, walk in "
    "and closed the door behind you.")
        option_door()
    else:
        print (required)
        option_yes()

def option_door():
    time.sleep(1)
    print("You see a little girl on the floor in front "
    "of a door ahead. It looks like she is looking "
    "for something. You see a pair of glasses "
    "on the ground. What do you do?")
    time.sleep(1)
    print ("""    A. Wave hi to her
    B. Grab the glasses
    C. Walk past her""")
    choice = input(">>> ")
    if choice in answer_A:
        print ("\nYou wave to the little girl. No response. "
    "You wave again. The little girl raised her head. She "
    "Surpised, she shouted: 'Oh no! A monster!'. "
    "Her hands turn into claws and stab you in the "
    "heart. \n\nYou died!")
    elif choice in answer_B:
        print ("You picked up the glasses and handed it to "
    "the girl. She smiled, took the glassses, and put it on. "
    "'Thank you very much! I can see again!' She waved "
    "goodbye and disappeared in thin air. The door opened. You moved on "
    "to the next room. Inside, you found three treasure "
    "chests side by side each other. Which do you pick?")
        option_glasses()
    elif choice in answer_C:
        print ("\nYou walk past the little girl. Suddenly, "
    "the little girl saw you at the corner of her eyes. "
    "She yelled 'Who is there?!'. She turned her hands "
    "into claws and cut your torso. You fell on the ground "
    "and bled to death. \n\nGame Over!")
    else:
        print (required)
        option_door()

def option_glasses():
    time.sleep(1)
    print ("""    A. Left
    B. Middle
    C. Right""")
    choice = input(">>> ")
    if choice in answer_A:
        print ("\nYou opened the left treasure chest. Inside is "
    "a gold crown covered in rare jewels. It is glistening "
    "under the light. Suddenly, you hear rumbling sounds. "
    "The wall in the back of the room opens an exit. You "
    "left the dungeon with your treasure. \n\nYou won!")
    elif choice in answer_B:
        print ("You opened the middle treasure chest. Inside is "
    "filled with very poisonous scorpons. All of them "
    "swarmed in and stinged you. \n\nYou died!")
    elif choice in answer_C:
        print ("\nYou opened the right treasure chest. Inside was "
    "empty. Suddenly, you heard the door locked and spikes popped up "
    "on the ceiling and walls. The ceiling and walls were "
    "closing in on you. There was no where to escape. "
    "\n\nGame Over!")


# In[ ]:


start()


# In[ ]:




