from tkinter import *

class PixelApp:
    
    def __init__(self, root):
        self.root = root
        self.root.title("Pixel Art")
        
        cell_length = 50
        grid_width = 20
        grid_height = 10
        
        self.drawing_grid = Canvas(self.root)    
        self.drawing_grid.grid(column=0, row=0, sticky=(N, E, S, W))
        
        self.cells = []
        for i in range (0, grid_height):
            for j in range (0, grid_width):
                cell = Frame(self.drawing_grid, width=cell_length, 
                     height=cell_length, 
                     bg="white", 
                     highlightbackground="black", 
                     highlightcolor="black", 
                     highlightthickness="1"
                     )
                cell.grid(column=j, row=i,)
                cell.bind("<Button-1>", self.tap_cell)
                self.cells.append(cell)
        
        
    def tap_cell(self, event):
        print("Cell Taped")
       
        
root = Tk()
PixelApp(root)
root.mainloop()        