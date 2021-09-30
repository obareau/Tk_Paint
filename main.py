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
        
        # Control frame
        control_frame = Frame(self.root, height=cell_length)
        control_frame.grid(column=0, row=1 , sticky=(N, E, S, W))
        
        # Widgets
        new_button = Button(control_frame, text="New")
        new_button.grid(column=0, row=0)
        
        save_button = Button(control_frame, text="Save")
        save_button.grid(column=2, row=0)
        
        pen_button = Button(control_frame, text="Pen")
        pen_button.grid(column=8, row=0)
        
        erase_button = Button(control_frame, text="Erase")
        erase_button.grid(column=10, row=0)
        
    def tap_cell(self, event):
        print("Cell Taped")
       
        
root = Tk()
PixelApp(root)
root.mainloop()        