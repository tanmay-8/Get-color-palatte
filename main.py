from functools import partial
import math
import extcolors
from tkinter import CENTER, Button, Label,Tk,filedialog
from PIL import Image
import pyperclip
import tkinter.messagebox as messagebox

FONT_NAME = "Courier"


def rgb_to_hex(colors):
    hexcolors = []
    for i in colors:
        hexcolor = '%02x%02x%02x' % i[0]
        hexcolors.append(f"#{hexcolor}")
    return hexcolors

def copy(i):
    pyperclip.copy(i)
    messagebox.showinfo("Copied",f"Copied {i}")


main = Tk()
main.withdraw()
image = filedialog.askopenfilename(initialdir=r"C:\Images",title="Select Image")
img = Image.open(image)
rgbcolors, pixel_count = extcolors.extract_from_image(img)
hexcolors = rgb_to_hex(rgbcolors)

height = math.ceil(len(hexcolors)/9)*140+20

main2 = Tk()
main2.geometry(f"1190x{height}")

xcori = 10
ycori = 10
buttons = []
for i in hexcolors:
    if xcori<=1105:
        try:
            b1 =  Button(master=main2,text=i,font=(FONT_NAME,15,""),fg="black",bg=i,anchor=CENTER,command=partial(copy,i))
            b1.place(x=xcori,y=ycori,width=120,height=120)
            buttons.append(b1)
        except:
            b1 =  Button(master=main2,text=f"{i}\n(Unidentified)",font=(FONT_NAME,10,""),fg="black",bg="white",anchor=CENTER,command=partial(copy,i))
            b1.place(x=xcori,y=ycori,width=120,height=120)
            buttons.append(b1)
        xcori+=130
    else:
        xcori = 10
        ycori += 130
        try:
            b1 =  Button(master=main2,text=i,font=(FONT_NAME,15,""),fg="black",bg=i,anchor=CENTER,command=partial(copy,i))
            b1.place(x=xcori,y=ycori,width=120,height=120)
            buttons.append(b1)
        except:
            b1 =  Button(master=main2,text=f"{i}\n(Unidentified)",font=(FONT_NAME,10,""),fg="black",bg="white",anchor=CENTER,command=partial(copy,i))
            b1.place(x=xcori,y=ycori,width=120,height=120)
            buttons.append(b1)
        xcori += 130
        
l1 = Label(text="Click On Color To Copy Hex Code",master=main2,font=(FONT_NAME,15,""),fg="black",bg="white",anchor=CENTER)
l1.place(x=10,y=ycori+130,width=1150,height=20)
main2.mainloop()

print(hexcolors)
