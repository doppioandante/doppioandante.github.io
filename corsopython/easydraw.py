import tkinter

__all__ = ["create_window", "draw_line", "draw_rectangle", "draw_pixel", "clear"]

_cv = None


def create_window(width, height, title = "easydraw"):
    """
    Create a window with specified dimensions.
    Must be called at the beginning, only one time.
    """
    global _cv

    if _cv is not None:
        return
    
    master = tkinter.Tk()
    master.resizable(0, 0)
    master.title(title)
    _cv = tkinter.Canvas(master, width=width, height=height)
    _cv.pack()

def draw_line(x, y, w, z, color):
    """
    Draw a line from point (x,y) to point (w,z) of the specified color
    """
    _cv.create_line(x, y, w, z, fill=color)

def draw_rectangle(x, y, width, height, color):
    """
    Draw a rectangle with top-left corner in (x,y), with specified width, height (in pixels) and color
    """
    _cv.create_rectangle(x, y, x+width, y+height, state=tkinter.DISABLED, outline='', fill=color)

def draw_pixel(x, y, color):
    """ Set pixel (x, y) to color"""
    draw_rectangle(x, y, 1, 1, color)

def clear():
    """
    Clears the screen
    """
    _cv.delete("all")
    


#mainloop()
