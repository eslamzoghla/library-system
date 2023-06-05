from start_screen import start_screen
from app import App

root = App()


def center(e):
    w = int(root.winfo_width() / 3.2)  # get root width and scale it ( in pixels )
    s = 'BFCAI Library '.rjust(w // 2)
    root.title(s)


root.bind("<Configure>", center)  # called when window resized

root.setSize(900, 800)
root.resizable(False, False)
root.goToScreen(start_screen)
root.mainloop()
