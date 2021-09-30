from tkinter import *

class PixelApp:
    
    def __init__(self, root):
        self.root = root
        self.root.title("Pixel Art")
        
        cell_length = 50
        
        self.drawing_grid = Canvas(self.root)    
        self.drawing_grid.grid(column=0, row=0, sticky=(N, E, S, W))
        
        cell = Frame(self.drawing_grid, width=cell_length, height=cell_length, bg="white", highlightbackground="black", hilightcolor="black", highlightthickness="1")
   
        
root = Tk()
PixelApp(root)
root.mainloop()        