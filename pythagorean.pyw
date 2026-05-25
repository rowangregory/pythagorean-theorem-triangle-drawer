# import turtle and math module
import turtle, math, pyautogui
artist = turtle.Turtle()
# functions for less code to write
def drawTriangle(l1, l2, h):
    artist.forward(l1 * 30)
    artist.backward(l1 * 15)
    artist.write(l1)
    artist.backward(l1 * 15)
    # draw b
    artist.left(90)
    artist.forward(l2 * 15)
    artist.write(l2)
    # draw c
    artist.right(45)
    artist.goto(l1 * 30, 0)
    artist.up()
    artist.goto(h * 10, h * 10)
    artist.down()
    artist.write(h)
    # display mathematical information
    pyautogui.alert(f'''Here is the information considering the variables:
a = {l1}
b = {l2}
c = {h}''',
"Mathematical Info")
# introduce to user
pyautogui.confirm('This is a right triangle drawer! Please input at least two numbers.')
# prompt user to fill in values
a = pyautogui.prompt("This is the length of the first side of the triangle: ")
b = pyautogui.prompt("This is the length of the second side of the triangle: ")
c = pyautogui.prompt("This is the length of the third and largest side of the triangle: ")
# try to convert string response into integer
try:
    a = int(a)
    b = int(b)
    c = int(c)
except:
    # python doesnt like it when i do this without the try and except blocks for some whatever reason - Rowan
    print("You typed ''")
# math evaluation
if (b) and (c) and (a):
    b2 = b ** 2
    c2 = c ** 2
    a2 = a ** 2
    if a2 + b2 != c2:
        pyautogui.alert("The values you have provided do not make a right triangle"
        , "Restart")
    else:
        drawTriangle(a, b, c)
elif (b) and (not a) and (c):
    a2 = c ** 2 - b ** 2
    a = math.sqrt(a2)
    # draw the triangle
    drawTriangle(a, b, c)
elif (a) and (not b) and (c):
    # uhh... idk what to say here 
    b2 = c * c - a * a
    b = math.sqrt(b2)
    drawTriangle(a, b, c)
elif (a) and (not c) and (b):
    c2 = a ** 2 + b ** 2
    c = math.sqrt(c2)
    drawTriangle(a, b, c)
else:
    pyautogui.alert("You need to put in at least two values", "Restart")
turtle.done()
