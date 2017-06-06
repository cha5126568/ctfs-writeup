from PIL import Image
import sys
PATH = 'test.png'
im = Image.open(PATH)
pixels = im.load()
for i in range(0,31):
 sys.stdout.write(chr(pixels[i, 0][0]))
