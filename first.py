import random
from random import randint
import tkinter as tk

#returns a random upper case letter
def uppercase():
	upper = chr(random.randint(65,90))
	return upper
#returns a random lower case letter
def lowercase():
	lower = chr(random.randint(97,122))
	return lower
#returns a random number
def number():
	num = chr(random.randint(48,57))
	return num

#number()
#lowercase()
#uppercase()


def generatePass():
	#deletes whatever was in the entry, maybe something the user typed or an unwanted password
	entry.delete(0,tk.END)

	#"randomly" decides on the length of password 
	length = randint(7,15)

	password = ""
	#generates the password
	for i in range(length):
		dec = randint(0,2)
		if dec == 0:
			password = password + str(number())
		elif dec == 1:
			password = password + str(uppercase())
		else:
			password = password + str(lowercase())
	#displays password in the entry
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