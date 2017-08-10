from PIL import Image
import sys
PATH = 'Z:\\real.png'
im = Image.open(PATH)
pixels = im.load()
f = open("data.txt")

lines = f.readlines()
for line in lines:
        AA = line.split(" - ")
        BB = AA[1].split(" ")
        x = int(AA[0])
        y = int(BB[0])
        if BB[1] == "Black\n":
                pixels[x,y] = (0,0,0)
                
        else:
                pixels[x,y] = (255,255,255)

im.save("test2.png")
