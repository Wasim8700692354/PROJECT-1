from tkinter import *

main = Tk()
main.title("Python Calculator")
main.geometry("420x450")

operator = ""
input_value = StringVar()
display_text = Entry(main, font=("arial",20,"bold"),textvariable=input_value,bd=30,insertwidth=4,
                     bg="sky blue", justify=LEFT)
display_text.grid(columnspan=4)

main.mainloop()