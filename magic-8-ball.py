import random
import time
import sys
import tkinter as tk
#Response list
lst = []
lst.extend([" It is certain.",
			"It is decidedly\n          so.",
			"Without\na doubt.",
			"       Yes,\n  definitely.",
			"  You may\n  rely on it.",
			" As I see it,\n       yes.",
			" Most likely.",
			" Outlook good.",
			"    Yes.",
			"  Signs point\n      to yes.",
			"  Reply hazy,\n   try again.",
			"   Ask again\n      later.",
			"   Better not\ntell you now.",
			" Cannot predict\n          now.",
			" Concentrate\n         and\n    ask again.",
			"  Don't count\n        on it.",
			" My reply is no.",
			"  My sources\n     say no.",
			" Outlook not so\n         good.",
			" Very doubtful.",
			"Duh."])
def deleteTags():
	canvas.delete("all")
	canvas.create_oval(10,10, w-10, h-10, fill="black", outline="#1b1b1c")
def after(x, y):
	window.after(x, y)
def bind():
	canvas.bind("<Button-1>", clicked)	
def unbind():
	canvas.unbind("<Button-1>")	
def clicked(event):
	deleteTags()
	unbind()
	after(25, removeBackside)
	after(50, removeBackside2)
	after(100, removeBackside3)
	after(150, barely)
	after(200, barely2)
	after(250, semi)
	after(300, semi2)
	after(350, almost)
	after(400, almost2)
	after(450, response)
	after(500, bind)
def removeBackside():
	deleteTags()
	canvas.create_oval(130,180, w-250, h-180, fill="#1b1b1c", tag="backside-inner")
	canvas.create_text(230,300,fill="white",font="Calibri 70 bold", text="8", tag="backside")
def removeBackside2():
	deleteTags()
	canvas.create_oval(30,180, w-350, h-180, fill="#1b1b1c", tag="backside-inner")
	canvas.create_text(100,300,fill="white",font="Calibri 60 bold", text="8", tag="backside")	
def removeBackside3():
	deleteTags()
	canvas.create_oval(10,210, w-450, h-210, fill="#1b1b1c", tag="backside-inner")
	canvas.create_text(50,300,fill="white",font="Calibri 50 bold", text="8", tag="backside")	

def barely():
	deleteTags()
	canvas.create_oval(500,200, w-10, h-210, fill="#1b1b1c", tag="inner")
def barely2():
	deleteTags()
	canvas.create_oval(400,190, w-40, h-190, fill="#1b1b1c", tag="inner")
def semi():
	deleteTags()
	canvas.create_oval(300,180, w-55, h-180, fill="#1b1b1c", tag="inner")
def semi2():
	deleteTags()
	canvas.create_oval(250,180, w-70, h-180, fill="#1b1b1c", tag="inner")
def almost():
	deleteTags()
	canvas.create_oval(230,180, w-90, h-180, fill="#1b1b1c", tag="inner")
def almost2():
	deleteTags()
	canvas.create_oval(210,180, w-120, h-180, fill="#1b1b1c", tag="inner")
def response():
	deleteTags()
	canvas.create_oval(180,180, w-180, h-180, fill="#1b1b1c", tag="inner")
	#Make Triangle
	points = [225, 255, 375, 255, 300, 375]
	canvas.create_polygon(points,fill="blue", tag="triangle")
	# generate random response
	r = random.randint(0,(len(lst)-1))
	response = lst[r]
	canvas.delete(canvas.gettags("response"))
	canvas.create_text(300,300,fill="white",font="Calibri 7 bold italic", text=response, tag="response")
	canvas.pack()
#Define application
window = tk.Tk()
#Create window with modified starting position
window.title("Magic 8 Ball")
#Place window in middle
w = 600 
h = 600 
ws = window.winfo_screenwidth() 
hs = window.winfo_screenheight() 
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
window.geometry('%dx%d+%d+%d' % (w, h, x, y))

#Make canvas object
canvas = tk.Canvas(window, width = w, height = h, bg='#c2d1ea', highlightbackground="#c2d1ea")
#Make Eightball
canvas.create_oval(10,10, w-10, h-10, fill="black", outline="#1b1b1c")
canvas.create_oval(180,180, w-180, h-180, fill="#1b1b1c", tag="backside-inner")
canvas.create_text(300,300,fill="white",font="Calibri 70 bold", text="8", tag="backside")
canvas.pack()

####comment for single response testing###
canvas.bind("<Button-1>", clicked)
#### unlock for testing single response ####
# points = [225, 255, 375, 255, 300, 375]
# canvas.create_polygon(points,fill="blue", tag="triangle")
# canvas.create_text(300,300,fill="white",font="Calibri 7 bold", text=lst[15], tag="response")

window.mainloop()
