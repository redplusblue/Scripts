# Author: Samir Kabra
# This program can be used to read a pdf aloud using edge's read aloud features.

import time
import os
import pyautogui as keyboard
import webbrowser

def openDoc():
    """
    This function uses the webbrowser library to open the .pdf file.
    **Can also be used to open a weblink or another program
    """
    path = "test.pdf"
    webbrowser.open_new(path)
    print("File/Link Opened Successfully.")

def keyRunner():
    """
    This function emulates the keyboard shortcuts to run the read aloud feature of edge.
    ctrl + shift + U
    """
    # Delay to account for the time taken for the file to open
    time.sleep(5)

    # Alt - Tab keys (optional) if the pdf file isnt on top
    #keyboard.keyDown("alt")
    #time.sleep(0.2)
    #keyboard.keyDown("tab")
    #time.sleep(0.2)
    #keyboard.keyUp("alt")
    #time.sleep(0.2)
    #keyboard.keyUp("tab")
    #time.sleep(0.2)

    #Keydowns first to emulate simultaneous keypresses.
    keyboard.keyDown("ctrl")
    time.sleep(0.2)
    keyboard.keyDown("shift")
    time.sleep(0.2)
    keyboard.press("u")
    time.sleep(0.2)
    keyboard.keyUp("ctrl")
    time.sleep(0.2)
    keyboard.keyUp("shift")

if __name__ == '__main__':
    print("Opening Document/Link")
    openDoc()
    print("Simulating Keypress for Edge")
    keyRunner()
    print("Done!")
    time.sleep(5)
    
