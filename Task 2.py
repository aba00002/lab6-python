from gfxhat import lcd, backlight


backlight.set_all(255, 255, 200)
backlight.show()
lcd.clear()
lcd.show()

def clearScreen(lcd):
    lcd.clear()
    lcd.show()

#a function displayObject
def displayObject(obj,lcd,x,y):
    b = x
    for h in object:
        for a in h:
            lcd.set_pixel(x,y,a)
            lcd.show()
            x = x + 1
            if x == 128:
                x = 0
        y = y + 1
        if y == 64:
            y = 0
            x = b


#Object to test
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

#Object to test
pm = [[0,0,0,1,1,1,1,1,0,0,0],
[0,0,1,1,1,1,1,1,1,0,0],
[0,1,1,1,1,1,1,1,1,1,0],
[1,1,1,1,1,1,1,1,0,0,0],
[1,1,1,1,1,1,1,0,0,0,0],
[1,1,1,1,1,1,0,0,0,0,0],
[1,1,1,1,1,1,0,0,0,0,0],
[1,1,1,1,1,1,1,0,0,0,0],
[1,1,1,1,1,1,1,1,0,0,0],
[0,1,1,1,1,1,1,1,1,1,0],
[0,0,1,1,1,1,1,1,1,0,0],
[0,0,0,1,1,1,1,1,0,0,0]
]

#a program that tests your displayObject function. The program prompts the user for the x,y coordinates, the object to display and displays it.
x = int(input('Select where list or tuple will be displayed: '))
while x > 127 or x < 0:
    x = int(input('key a value between the range of 0 and 127 for x axis: '))

y = int(input('Select where list or tuple will be displayed: '))
while y > 63 or y < 0:
    y = int(input('key a value between the range of 0 and 63 for y axis: '))

#to call the function for first object
clearScreen()
displayObject(f1,lcd,x,y)
#to call the function for first object
clearScreen()
displayObject(pm,lcd,x,y)