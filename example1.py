import tkinter as tk
from tkinter import StringVar

root = tk.Tk() 
rbvar = StringVar() 
rbvar.set(" ") 

# control variable
var = tk.IntVar(root, 0)
# group of radiobuttons
for i in range(1,4):
 tk.Radiobutton(root, text='Choice %i' % i, value=i, variable=var).pack()
tk.Button(root, text='Print choice', command=lambda: print(var.get())).pack()

rb1 = tk.Radiobutton(root, text="Option 1", variable=rbvar, value='a', indicatoron=0) 
rb1.pack() 
rb2 = tk.Radiobutton(root, text="Option 2", variable=rbvar, value='b', indicatoron=0) 
rb2.pack()

root.mainloop()