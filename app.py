from tkinter import *
import backend as db


class App(Tk):
    def __init__(self):
        super().__init__()
        self.active_screen = None

    def setSize(self, width, height):
        screenWidth = self.winfo_screenwidth()
        screenHeight = self.winfo_screenheight()
        x = ((screenWidth - width) // 2)
        y = ((screenHeight - height) // 2)
        self.geometry(f'{width}x{height}+{x}+{y}')

    def goToScreen(self, Screen):
        if self.active_screen:
            self.active_screen.destroy()
        self.active_screen = Screen(self)
        self.active_screen.pack(expand=True, fill=BOTH)
