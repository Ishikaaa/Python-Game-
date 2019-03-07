from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
a1=Tk()
a1.geometry("700x700+330+0")
a1.title("Maze Game")
image1 = Image.open('mg_front_page_1.jpg')
img_copy = image1.copy()
image3 = ImageTk.PhotoImage(image1)
def BB1():
  a1.destroy()
  import maze_game_mode
  print("Hiiii")
def BB2():
  if messagebox.askokcancel("Quit", "Do you want to quit?"):
    a1.destroy()
def Resize_image(event):
    new_width = 700
    new_height = 700
    image4 = img_copy.resize((new_width, new_height))
    image5 = ImageTk.PhotoImage(image4)
    label.config(image=image5)
    label.image = image5
    # avoid garbage collection
label = Label(a1, image=image3);label.pack(fill=BOTH, expand = YES);label.bind('<Configure>',Resize_image)
B1=Button(a1,text="New Game",command= BB1, width=15, height = 3,bg='#b380ff',cursor="dot");B1.place(x=295,y=420)
B2=Button(a1,text="Exit",command= BB2, width=15, height=3,bg='#b380ff',cursor="dot");B2.place(x=295,y=542)
a1.mainloop()



