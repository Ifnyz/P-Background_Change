import os
import sys
import ctypes
import random

class Main:
    def __init__(self):
        self.path = 'C:\\Users\\X495641\\Desktop'
        for root, directories, files in os.walk(os.path.join(self.path, 'background')):
            self.background = [file.lower() for file in files if file.endswith(('.png', '.jpg', '.jpeg'))]

        ctypes.windll.user32.SystemParametersInfoW(20, 0, os.path.join(self.path, 'background', random.choice(self.background)) , 0)

application = Main()

