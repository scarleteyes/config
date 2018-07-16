import sys
import os
import datetime

import pyauto
from keyhac import *

'''
Remap Windows shortcuts like mac with Keyhac.

Keyhac
https://sites.google.com/site/craftware/keyhac-en
'''

def configure(keymap):

    # --------------------------------------------------------------------
    # Text editer setting for editting config.py file
    keymap.editor = "notepad.exe"

    # --------------------------------------------------------------------
    # Customizing the display

    # Font
    keymap.setFont( "MS Gothic", 12 )

    # Theme
    keymap.setTheme("black")

    # --------------------------------------------------------------------

    # Global keymap which affects any windows
    keymap_global = keymap.defineWindowKeymap()
    # Move
    keymap_global[ "C-P" ] = "Up"                  # Move cursor up
    keymap_global[ "C-N" ] = "Down"                # Move cursor down
    keymap_global[ "C-F" ] = "Right"               # Move cursor right
    keymap_global[ "C-B" ] = "Left"                # Move cursor left
    keymap_global[ "C-A" ] = "Home"                # Move to beginning of line
    keymap_global[ "C-E" ] = "End"                 # Move to end of line
    keymap_global[ "Shift-C-P" ] = "Shift-Up"      # Move cursor up and select
    keymap_global[ "Shift-C-N" ] = "Shift-Down"    # Move cursor down and select
    keymap_global[ "Shift-C-F" ] = "Shift-Right"   # Move cursor right and select
    keymap_global[ "Shift-C-B" ] = "Shift-Left"    # Move cursor left and select
    keymap_global[ "Shift-C-A" ] = "Shift-Home"    # Move to beginning of line and select
    keymap_global[ "Shift-C-E" ] = "Shift-End"     # Move to end of line and select
    # File
    keymap_global[ "A-N" ] = "C-N"                 # New File
    keymap_global[ "A-S" ] = "C-S"                 # Save
    keymap_global[ "Shift-A-S" ] = "A-F","A-A"     # Save as
    keymap_global[ "A-W"] = "C-W"                  # Close current tab
    keymap_global[ "A-Q" ] = "A-F4"                # Quit
    # Edit
    keymap_global[ "LA-F" ] = "C-F"                # Search
    keymap_global[ "LA-RA-F" ] = "C-H"             # Replace
    keymap_global[ "A-Z" ] = "C-Z"                 # Undo
    keymap_global[ "Shift-A-Z" ] = "C-Y"           # Redo
    keymap_global[ "A-A" ] = "C-A"                 # Select all
    keymap_global[ "A-X" ] = "C-X"                 # Cut
    keymap_global[ "A-C" ] = "C-C"                 # Copy
    keymap_global[ "A-V" ] = "C-V"                 # Paste
    keymap_global[ "C-D" ] = "Delete"              # Delete
    keymap_global[ "C-H" ] = "Back"                # Backspace
    keymap_global[ "C-K" ] = "S-End","C-X"         # Removing following text
    # Other
    keymap_global[ "A-P" ] = "C-P"
    keymap_global[ "Shift-A-P" ] = "Shift-C-P"
