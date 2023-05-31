import tkinter as tk
from PIL import Image,ImageTk

#settings:
x = 3 # Sprite Sheet Column (0-3)
y = 3 # Sprite Sheet Row (0-7)

w = tk.Tk()
w.attributes("-topmost",True)
w.geometry("400x300")

c = tk.Canvas(width=380,height=280)
c.pack()
i=0
def getSprite(x,y):
# sk.png sprite sheet is 384 x 384 pixels, with 12 across and 8 down.
# each image is 32 x 48 pixels    
    img = Image.open("assets/skt.png").convert("RGBA")
    xi = x*32
    yi = y*48
    img2 = img.crop([xi,yi,xi+32,yi+48])
    return ImageTk.PhotoImage(img2)    

def skelUpdate():
    global i

    i+=1
    i%=len(skel)
    c.itemconfig(img,image=skel[i])
    w.after(200,skelUpdate)
image = tk.PhotoImage(file="assets/skt.png")


skel=[]
#There are 3 sprite images:
# left foot forward
# neutral
# right foot forward
# we load all 3 sprites and then also add in the neutral as a 4th sprite
for i in range(3):
    firstX = i + 3*x # there are 3 sprites in an animation
    skel.append( getSprite(firstX,y))
skel.append( getSprite(firstX + 1,y))

#create the sprite with the first image and then update it after 200 milliseconds
img = c.create_image(32,48,image=skel[0])
w.after(200,skelUpdate)


w.mainloop()