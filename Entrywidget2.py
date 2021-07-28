import tkinter as tk

window = tk.Tk()
#membuat path entry
entry = tk.Entry(window, width=10)
entry.pack()
#memasukan ke variabel masukan 
masukan = entry.get()
window.mainloop()