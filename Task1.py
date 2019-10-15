from gfxhat import lcd,  fonts, backlight
from PIL import Image, ImageFont, ImageDraw
import click


def clearScreen(lcd):
    lcd.clear()
    lcd.show()

def displayText(text,lcd,x,y):
    lcd.clear()
    width, height = lcd.dimensions()
    image = Image.new('P', (width, height))
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(fonts.AmaticSCBold, 24)
    w, h = font.getsize(text)
    draw.text((x,y), text, 1, font)
    for x1 in range(x,x+w):
        for y1 in range(y,y+h):
            pixel = image.getpixel((x1, y1))
            lcd.set_pixel(x1, y1, pixel)
    lcd.show()

y = 50
x = 50

import click
clearScreen(lcd)
backlight.set_all(255,255,100)
backlight.show()
displayText("Etch a Sketch",lcd,24,24)
key = click.getchar()
while key == '\x1b[A' or key == '\x1b[B' or key == '\x1b[C' or key == '\x1b[D' or key == 's' or key == 'q':
    
    if key == '\x1b[A':
        if key == 0:
            y = 64
        y = y - 1
        lcd.set_pixel(x,y,1)
        lcd.show()
        key = click.getchar()

    if key == '\x1b[B':
        if key == 63:
            y = -1
        y = y + 1
        lcd.set_pixel(x,y,1)
        lcd.show()
        key = click.getchar()
    
    if key ==  '\x1b[C':
        if x == 127:
            x = -1
        x = x + 1
        lcd.set_pixel(x,y,1)
        lcd.show()
        key = click.getchar()

    if key == '\x1b[D':
        if x == 0:
            x = 128
        x = x - 1
        lcd.set_pixel(x,y,1)
        lcd.show()
        key = click.getchar()

    if key == 's':
        lcd.clear()
        lcd.show()
        backlight.set_all(255,255,100)
        backlight.show()
        x = 50
        y = 50
        key = click.getchar()
    
    if key == 'q':
        lcd.clear()
        lcd.show()
        backlight.set_all(0,0,0)
        backlight.show()
        break