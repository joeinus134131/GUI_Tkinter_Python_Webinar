import tkinter as tk #python3

root = tk.Tk()
#ini window bawaan atau defaultnya
label1 = tk.Label(root, text="""bawaannya""")
label1.pack()
#Top levelnya
extra_window = tk.Toplevel(root)
label2 = tk.Label(extra_window, text="""ekstra windownya""")
label2.pack()
root.mainloop()