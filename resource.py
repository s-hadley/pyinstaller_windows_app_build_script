##########################################################
#*** Resource Path Location Function ****
##########################################################

import sys
import os

# PyInstaller stores images files in a temp folder during app operation
# This function returns a full path to the file, so that it can be used by your app (when your app is run by PyInstaller)
# https://stackoverflow.com/questions/31836104/pyinstaller-and-onefile-how-to-include-an-image-in-the-exe-file

def get_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)