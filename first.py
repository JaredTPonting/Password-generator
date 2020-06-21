import random
from random import randint
import tkinter as tk

def shuffle(string):
	templist = list(string)
	random.shuffle(templist)
	return ''.join(templist)




def uppercase():
	upper = chr(random.randint(65,90))
	return upper

def lowercase():
	lower = chr(random.randint(97,122))
	return lower

def number():
	num = chr(random.randint(48,57))
	return num

#number()
#lowercase()
#uppercase()

funcCall = ["number()", "uppercase()", "lowercase()"]

funcCall[randint(0,2)]

def generatePass():
	entry.delete(0,tk.END)
	length = randint(7,15)
	password = ""
	for i in range(length):
		dec = randint(0,2)
		if dec == 0:
			password = password + str(number())
		elif dec == 1:
			password = password + str(uppercase())
		else:
			password = password + str(lowercase())
	entry.insert(0,password)




root = tk.Tk()

canvas = tk.Canvas(root)
canvas.place(relwidth = 1, relheight = 1, relx = 0,rely=0)

button = tk.Button(canvas, text = "Generate Password!", command = generatePass)
button.place(relx = 0, rely = 0.5, relwidth = 1, relheight = 0.5)

label = tk.Label(canvas)
label.place(relx=0,rely=0,relwidth = 1,relheight = 0.5)

entry = tk.Entry(canvas)
entry.place(relx=0,rely=0,relwidth = 1,relheight = 0.5)

root.mainloop()