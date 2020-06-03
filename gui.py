from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import time
import biblioteka


main = Tk()

def open():
    global img
    global photo
    main.filename = filedialog.askopenfilename(initialdir="/",
                               title="Select A File", filetypes=(("jpg files", "*.jpg"), ("png files", "*.png"),("bmp files", "*.bmp"), ("all files", "*.*")))
    photo = Image.open(main.filename)
    img = ImageTk.PhotoImage(photo)

def show():
    global img
    global photo
    lab1.configure(image=img)
    lab1.image = img

def change():
    global img
    global photo
    start = time.time()
    x = biblioteka.ImageProcessing()
    obraz = x.to_main_colors(main.filename)
    end = time.time()
    print(f"Czas konwersji obrazu: {end-start} [s]")
    img = ImageTk.PhotoImage(obraz)
    lab1.configure(image=img)
    lab1.image = img


B0 = Button(main, text ="Wczytaj obraz", command = open)
B0.pack()
B1 = Button(main, text ="Zmien kolor", command = change)
B1.pack()
B2 = Button(main, text ="Wyswietl obraz", command = show)
B2.pack()
lab1 = Label(main, image='')
lab1.pack(expand="no")



mainloop()