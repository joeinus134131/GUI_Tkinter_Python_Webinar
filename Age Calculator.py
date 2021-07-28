import datetime
import tkinter as tk
from PIL import Image,ImageTk

window=tk.Tk()
window.geometry("300x500")
window.title(" Age Calculator App ")
#window.configure(bg="#FFE873")  untuk membuat warna background

image=Image.open("kucingasli.png")
image.thumbnail((200,500),Image.ANTIALIAS)
photo=ImageTk.PhotoImage(image)
label_image=tk.Label(image=photo)
label_image.grid(column=1,row=0)

#Tampilan Tulisan Judul 
name = tk.Label(text = "Nama")
name.grid(column=0,row=1)
year = tk.Label(text = "Tahun")
year.grid(column=0,row=2)
month = tk.Label(text = "Bulan")
month.grid(column=0,row=3)
date = tk.Label(text = "Tanggal")
date.grid(column=0,row=4)

#Entry data lahir dan nama
nameEntry = tk.Entry()
nameEntry.grid(column=1,row=1)
yearEntry = tk.Entry()
yearEntry.grid(column=1,row=2)
monthEntry = tk.Entry()
monthEntry.grid(column=1,row=3)
dateEntry = tk.Entry()
dateEntry.grid(column=1,row=4)

#fungsi hitung usia
def getInput():
    name=nameEntry.get()
    datadiri = Person(name,datetime.date(int(yearEntry.get()),int(monthEntry.get()),int(dateEntry.get())))
    textArea = tk.Text(master=window,height=10,width=25)
    textArea.grid(column=1,row=6)
    answer = " Heyy {datadiri}!!!. Kamu sekarang berusia {age} tahun!!! ".format(datadiri=name, age=datadiri.age())
    textArea.insert(tk.END,answer)

#tombol hitung
button=tk.Button(window,text="Hitung",command=getInput,bg="pink")
button.grid(column=1,row=5)

#kelas untuk support data perhitungan usia
class Person:
    def __init__(self,name,birthdate):
        self.name = name
        self.birthdate = birthdate
    def age(self):
        today = datetime.date.today()
        age = today.year-self.birthdate.year
        return age

window.mainloop()




    
