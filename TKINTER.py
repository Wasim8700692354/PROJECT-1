from tkinter import *

def buttonClick(number):
    global operator
    operator = operator + str(number)
    input_value.set(operator)

def buttonClear():
    global operator    # by using "global function", we can execute the code for each function present within the calculator
    operator = ""
    input_value.set("")

def buttonEqual():
    global operator
    result = str(eval(operator))
    input_value.set(result)
    operator = ""


main = Tk()
menu = Menu(main)
main.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label='File',menu=filemenu) 
filemenu.add_command(label='New')
filemenu.add_command(label='Open...')
filemenu.add_separator()
filemenu.add_command(label='Exit', command=main.quit)
main.title("Python Calculator")
main.geometry("420x450")

operator = ""
input_value = StringVar()
display_text = Entry(main, font=("arial",25,"bold"), textvariable=input_value, bd=30, insertwidth=8,
                     bg="sky blue",justify=RIGHT)   # bd is border=30 #   justify=RIGHT is to instruct the text, from right
display_text.grid(columnspan=4)

# Row 1 - 7 8 9 +

key_7= Button(main, padx=16, bd=8, fg="black",font=("arial", 20, "bold"), text="7",command= lambda: buttonClick(7))
key_7.grid(row=1, column=0) 

key_8= Button(main, padx=16, bd=8, fg="black",font=("arial", 20, "bold"), text="8",command= lambda: buttonClick(8))
key_8.grid(row=1, column=1)

key_9= Button(main, padx=16, bd=8, fg="black",font=("arial", 20, "bold"), text="9",command= lambda: buttonClick(9))
key_9.grid(row=1, column=2)

key_add= Button(main, padx=16, bd=8, bg="red", fg="black",font=("arial", 20, "bold"), text="+", command= lambda: buttonClick("+"))
key_add.grid(row=1, column=3)

# Row 2 - 4 5 6 -

key_4= Button(main, padx=16, bd=8, fg="black",font=("arial", 20, "bold"), text="4",command= lambda: buttonClick(4))
key_4.grid(row=2, column=0)

key_5= Button(main, padx=16, bd=8, fg="black",font=("arial", 20, "bold"), text="5",command= lambda: buttonClick(5))
key_5.grid(row=2, column=1)

key_6= Button(main, padx=16, bd=8, fg="black",font=("arial", 20, "bold"), text="6",command= lambda: buttonClick(6))
key_6.grid(row=2, column=2)

key_sub= Button(main, padx=16, bd=8, bg="red", fg="black",font=("arial", 20, "bold"), text="-",command= lambda: buttonClick("-"))
key_sub.grid(row=2, column=3)

# Row 3 - 1 2 3 *

key_1= Button(main, padx=16, bd=8, fg="black",font=("arial", 20, "bold"), text="1",command= lambda: buttonClick(1))
key_1.grid(row=3, column=0)

key_2= Button(main, padx=16, bd=8, fg="black",font=("arial", 20, "bold"), text="2",command= lambda: buttonClick(2))
key_2.grid(row=3, column=1)

key_3= Button(main, padx=16, bd=8, fg="black",font=("arial", 20, "bold"), text="3",command= lambda: buttonClick(3))
key_3.grid(row=3, column=2)

key_mul= Button(main, padx=16, bd=8, bg="red", fg="black",font=("arial", 20, "bold"), text="*",command= lambda: buttonClick("*"))
key_mul.grid(row=3, column=3)

# Row 4 - 0 C = /

key_clear= Button(main, padx=16, bg="yellow", bd=8, fg="black",font=("arial", 20, "bold"), text="      Clear     ",command=buttonClear,
                  activebackground="yellow")
key_clear.grid(row=5, columnspan=4)

key_0= Button(main, padx=16, bd=8, fg="black",font=("arial", 20, "bold"), text="0",command= lambda: buttonClick(0))
key_0.grid(row=4, column=1)

key_equal= Button(main, padx=16, bd=8, bg="lightgreen", fg="black",font=("arial", 20, "bold"), text="=",command=buttonEqual)
key_equal.grid(row=4, column=2)

key_div= Button(main, padx=16, bd=8, bg="red", fg="black",font=("arial", 20, "bold"), text="/",command= lambda: buttonClick("/"))
key_div.grid(row=4, column=3)

# Row 5 - .

key_decimal= Button(main, padx=16, bd=8, bg="lightgreen", fg="black",font=("arial", 20, "bold"), text=".",command= lambda: buttonClick("."))
key_decimal.grid(row=4, column=0)

main.mainloop()