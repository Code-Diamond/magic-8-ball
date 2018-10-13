import random
import sys
import tkinter as tk
#define application and allow passingg cmd line args
window = tk.Tk() 
#create window with modified starting position
window.title("Magic 8 Ball")

# Create list of responses
lst = []
lst.extend(["It is certain." , "It is decidedly so." , "Without a doubt." , "Yes - definitely." , "You may rely on it." , "As I see it,\n     yes." , "Most likely." , "Outlook good." , "Yes." , "Signs point to yes." , "Reply hazy, try again" , "Ask again later." , "Better not tell you now." , "Cannot predict now." , "Concentrate and ask again." , "Don't count on it." , "My reply is no." , "My sources say no." , "Outlook not so good." , "Very doubtful."])

# generate random response
r = random.randint(0,(len(lst)-1))
response = lst[r]

#Place window in middle
w = 400 # width for the Tk root
h = 400 # height for the Tk root
# get screen width and height
ws = window.winfo_screenwidth() # width of the screen
hs = window.winfo_screenheight() # height of the screen
# calculate x and y coordinates for the Tk root window
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
window.geometry('%dx%d+%d+%d' % (w, h, x, y))

canvas = tk.Canvas(window, width = w, height = h, bg='white', highlightbackground="white")
canvas.create_oval(10,10, w-10, h-10, fill="black")
canvas.create_oval(120,120, w-120, h-120, fill="#1b1b1c")
points = [150, 170, 250, 170, 200, 250]
canvas.create_polygon(points,fill="blue")
canvas.create_text(200,200,fill="white",font="Times 8 italic bold", text=lst[5])
# canvas.create_triangle()
canvas.pack()


window.mainloop()
