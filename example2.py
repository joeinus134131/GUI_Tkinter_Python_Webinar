import tkinter as tk

window = tk.Tk()
text = tk.Text(window)
text.pack(side="left")
scroll_y = tk.Scrollbar(window, orient="vertical", command=text.yview)
scroll_y.pack(side="left", expand=True, fill="y")
text.configure(yscrollcommand=scroll_y.set)
window.mainloop()