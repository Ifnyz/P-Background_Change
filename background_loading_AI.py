import os
import ctypes
import random

class Main:
    def __init__(self):
        # Set the path to the user's desktop
        self.path = 'C:\\Users\\X495641\\Desktop'

        # Get a list of images in the 'background' subdirectory of the user's desktop
        images = []
        for root, directories, files in os.walk(os.path.join(self.path, 'background')):
            images = [file.lower() for file in files if file.endswith(('.png', '.jpg', '.jpeg'))]

        # Set the desktop background to a random image from the list
        if images:
            ctypes.windll.user32.SystemParametersInfoW(20, 0, os.path.join(self.path, 'background', random.choice(images)) , 0)

application = Main()
