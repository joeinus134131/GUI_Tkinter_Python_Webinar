from tkinter import *

root = Tk()

btn_fill = Button(root, text="Tombol fill")
btn_fill.pack(fill=X)

btn_expand = Button(root, text="Tombol expand")
btn_expand.pack(expand=YES)

btn_side = Button(root, text="Tombol side")
btn_side.pack(side=RIGHT)

root.mainloop()