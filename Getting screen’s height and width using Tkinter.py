# importing tkinter module
from tkinter import * from tkinter.ttk import *
 
# creating tkinter window
root = Tk()
 
# getting screen's height in pixels
height = root.winfo_screenheight()
 
# getting screen's width in pixels
width = root.winfo_screenwidth()
 
print("\n width x height = %d x %d (in pixels)\n" %(width, height))
# infinite loop
mainloop()
Output: 
 




  
Code #2: Getting height and width in mm. 
 

# importing tkinter module
from tkinter import * from tkinter.ttk import *
 
# creating tkinter window
root = Tk()
 
# getting screen's height in mm
height = root.winfo_screenmmheight()
 
# getting screen's width in mm
width = root.winfo_screenmmwidth()
 
print("\n width x height = %d x %d (in mm)\n" %(width, height))
# infinite loop
mainloop()
