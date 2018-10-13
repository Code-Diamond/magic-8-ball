import random
import time
import sys
import tkinter as tk
#define application and allow passingg cmd line args
window = tk.Tk()
#create window with modified starting position
window.title("Magic 8 Ball")
# Create list of responses
lst = []
#response list
lst.extend([" It is certain.",
			"It is decidedly\n          so.",
			"Without\na doubt.",
			"       Yes,\n  definitely.",
			"    You may\n  rely on it.",
			" As I see it,\n       yes.",
			"Most likely.",
			"Outlook good.",
			"    Yes.",
			"  Signs point\n      to yes.",
			"  Reply hazy,\n   try again.",
			"   Ask again\n      later.",
			"   Better not\ntell you now.",
			" Cannot predict\n          now.",
			" Concentrate and\n    ask again.",
			"  Don't count\n       on it.",
			" My reply is no.",
			"  My sources\n     say no.",
			" Outlook not so\n         good.",
			" Very doubtful."])
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
canvas = tk.Canvas(window, width = w, height = h, bg='#c2d1ea', highlightbackground="#c2d1ea")
canvas.create_oval(10,10, w-10, h-10, fill="black")
canvas.create_oval(120,120, w-120, h-120, fill="#1b1b1c")
points = [150, 170, 250, 170, 200, 250]
canvas.create_polygon(points,fill="blue")
# canvas.create_text(200,200,fill="white",font="Calibri 5 bold", text=lst[0], tag="response")
def update_response():
	# generate random response
	r = random.randint(0,(len(lst)-1))
	response = lst[r]
	canvas.delete(canvas.gettags("response"))
	canvas.create_text(200,200,fill="white",font="Calibri 5 bold italic", text=response, tag="response")
	#loop
	window.after(1000, update_response)
#Pack, start loops
canvas.pack()
update_response()
window.mainloop()
