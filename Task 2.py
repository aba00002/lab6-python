from gfxhat import lcd,  fonts, backlight
from PIL import Image, ImageFont, ImageDraw

h = 63
w = 127
backlight.set_all(255, 255, 200)
backlight.show()

def lcd():
    for a in range(h):
        if y >= 0:
            lcd.set_pixel(x,y-a,1)
        else:
            h = a
    for b in range (0,w):
        if x+b<=SW:
            lcd.set_pixel(x+b,y-h,1)
    else:
         w = b
    return (x+w,y-h)

def displayObject(obj,x,y):
    while x <=127 and y <= 63:
        for x1 in range(x,x+w):
            x = x+1
        for y1 in range(y,y+h):
            y = y+1
    

f1 =  [
[1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1],
[0,1,1,1,1,1,1,0],
[1,0,1,1,1,1,0,1],
[1,0,0,1,1,0,0,1],
[1,0,0,1,1,0,0,1],
[0,0,0,1,1,0,0,0],
[0,0,0,0,0,0,0,0]
]

displayObject(f1,10,10)