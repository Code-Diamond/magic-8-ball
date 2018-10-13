import random
# import sys
# import tkinter as tk
# #define application and allow passingg cmd line args
# window = tk.Tk() 
# #create window with modified starting position
# window.setWindowTitle("Magic 8 Ball")

# canvas = Canvas(window, width = 400, height = 400, bg='#332f28', highlightbackground="#332f28")

# Create list of responses
lst = []
lst.extend(["It is certain." , "It is decidedly so." , "Without a doubt." , "Yes - definitely." , "You may rely on it." , "As I see it, yes." , "Most likely." , "Outlook good." , "Yes." , "Signs point to yes." , "Reply hazy, try again" , "Ask again later." , "Better not tell you now." , "Cannot predict now." , "Concentrate and ask again." , "Don't count on it." , "My reply is no." , "My sources say no." , "Outlook not so good." , "Very doubtful."])

# generate random response
r = random.randint(0,(len(lst)-1))
response = lst[r]

#Place window in middle
# w = 395 # width for the Tk root
# h = 380 # height for the Tk root
# # get screen width and height
# ws = root.winfo_screenwidth() # width of the screen
# hs = root.winfo_screenheight() # height of the screen
# # calculate x and y coordinates for the Tk root window
# x = (ws/2) - (w/2)
# y = (hs/2) - (h/2)
window.setGeometry(0,0,500,300)
