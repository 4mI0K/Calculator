from tkinter import *

root = Tk()

root.title("Calculator")

entry = Entry(root, width=45, borderwidth=5)
entry.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


def buttonClick(number):
	currentnum = entry.get()
	entry.delete(0, END)
	entry.insert(0, currentnum + str(number))


def buttonClear():
	entry.delete(0, END)


def buttonAdd():
	global num1
	global math
	math = "addition"
	num1 = entry.get()
	entry.delete(0, END)


def buttonEquals():
	try:
		global math
		global num1
		num2 = entry.get()
		if math == "addition":
			entry.delete(0, END)
			entry.insert(0, str(int(num1) + int(num2)))
			math = ""
		elif math == "division":
			entry.delete(0, END)
			try:
				entry.insert(0, str(int(int(num1) / int(num2))))
			except:
				entry.insert(0, "Error: Cant Divide by 0")
			math = ""
		elif math == "subtraction":
			entry.delete(0, END)
			entry.insert(0, str(int(num1) - int(num2)))
			math = ""
		elif math == "multiplication":
			entry.delete(0, END)
			entry.insert(0, str(int(num1) * int(num2)))
			math = ""
	except:
		entry.delete(0, END)
		pass


def buttonDivide():
	global num1
	global math
	math = "division"
	num1 = entry.get()
	entry.delete(0, END)


def buttonSubtract():
	global num1
	global math
	math = "subtraction"
	num1 = entry.get()
	entry.delete(0, END)

def buttonMultiply():
	global num1
	global math
	math = "multiplication"
	num1 = entry.get()
	entry.delete(0, END)


button1 = Button(root, text="1", padx=40, pady=20, command=lambda: buttonClick(1))
button2 = Button(root, text="2", padx=40, pady=20, command=lambda: buttonClick(2))
button3 = Button(root, text="3", padx=40, pady=20, command=lambda: buttonClick(3))
button4 = Button(root, text="4", padx=40, pady=20, command=lambda: buttonClick(4))
button5 = Button(root, text="5", padx=40, pady=20, command=lambda: buttonClick(5))
button6 = Button(root, text="6", padx=40, pady=20, command=lambda: buttonClick(6))
button7 = Button(root, text="7", padx=40, pady=20, command=lambda: buttonClick(7))
button8 = Button(root, text="8", padx=40, pady=20, command=lambda: buttonClick(8))
button9 = Button(root, text="9", padx=40, pady=20, command=lambda: buttonClick(9))
button0 = Button(root, text="0", padx=40, pady=20, command=lambda: buttonClick(0))

buttonP = Button(root, text="+", padx=39, pady=20, command=buttonAdd)
buttonE = Button(root, text="=", padx=91, pady=20, command=buttonEquals)
buttonC = Button(root, text="C", padx=91, pady=20, command=buttonClear)

buttonD = Button(root, text="/", padx=41, pady=20, command=buttonDivide)
buttonS = Button(root, text="-", padx=40, pady=20, command=buttonSubtract)
buttonM = Button(root, text="*", padx=41, pady=20, command=buttonMultiply)


button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)

button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)

button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)

button0.grid(row=4, column=0)
buttonP.grid(row=5, column=0)
buttonC.grid(row=5, column=1, columnspan=2)

buttonE.grid(row=6, column=1, columnspan=2)
buttonS.grid(row=6, column=0)
buttonM.grid(row=4, column=1)
buttonD.grid(row=4, column=2)


root.mainloop()
