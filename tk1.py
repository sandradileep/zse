from tkinter import *

def btnclick(numbers):
    global operator
    operator=operator+str(numbers)
    num_input.set(operator)

def btnclear():
    global operator
    operator=""
    num_input.set("")

def equalclick():
    global operator
    s=str(eval(operator))
    num_input.set(s)
    operator=""

window=Tk()
window.geometry("450x500")
window.title("Calculator")
window.configure(bg="#AEB6BF")


num_input=StringVar()

operator=""

num_inputdisplay=Entry(window,font=('arial',20,'bold'),bd=22,textvariable=num_input,bg="pink",justify="left",width=21).place(x=24,y=20)

#--------------------------------------------------------------------------------------------------------------#

b7=Button(window,text="7",font=('bold'),bd=8,bg="black",fg="white",height="3",width="5",command=lambda:btnclick(7),relief="raised").place(x=50,y=100)

b8=Button(window,text="8",font="bold",bd=8,bg="black",fg="white",height="3",width="5",command=lambda:btnclick(8),relief="raised").place(x=130,y=100)

b9=Button(window,text="9",font="bold",bd=8,bg="black",fg="white",height="3",width="5",command=lambda:btnclick(9),relief="raised").place(x=210,y=100)

divide=Button(window,text="/",font="bold",bd=8,bg="red",fg="white",height="3",width="5",command=lambda:btnclick("/"),relief="raised").place(x=290,y=100)

#--------------------------------------------------------------------------------------------------------------#

b4=Button(window,text="4",font="bold",bd=8,bg="black",fg="white",height="3",width="5",command=lambda:btnclick(4),relief="raised").place(x=50,y=190)

b5=Button(window,text="5",font="bold",bd=8,bg="black",fg="white",height="3",width="5",command=lambda:btnclick(5),relief="raised").place(x=130,y=190)

b6=Button(window,text="6",font="bold",bd=8,bg="black",fg="white",height="3",width="5",command=lambda:btnclick(6),relief="raised").place(x=210,y=190)

multiply=Button(window,text="*",bd=8,font="bold",bg="red",fg="white",height="3",width="5",command=lambda:btnclick("*"),relief="raised").place(x=290,y=190)

#--------------------------------------------------------------------------------------------------------------#


b1=Button(window,text="1",font="bold",bd=8,bg="black",fg="white",height="3",width="5",command=lambda:btnclick(1),relief="raised").place(x=50,y=280)

b2=Button(window,text="2",font="bold",bd=8,bg="black",fg="white",height="3",width="5",command=lambda:btnclick(2),relief="raised").place(x=130,y=280)

b3=Button(window,text="3",font="bold",bd=8,bg="black",fg="white",height="3",width="5",command=lambda:btnclick(3),relief="raised").place(x=210,y=280)

substraction=Button(window,text="-",bd=8,font="bold",bg="red",fg="white",height="3",width="5",command=lambda:btnclick("-"),relief="raised").place(x=290,y=280)


#--------------------------------------------------------------------------------------------------------------#


b0=Button(window,text="0",font="bold",bd=8,bg="black",fg="white",height="3",width="5",command=lambda:btnclick(0),relief="raised").place(x=50,y=370)

c1=Button(window,text="clear",font="bold",bd=8,bg="black",fg="white",height="3",width="5",command=lambda:btnclear(),relief="raised").place(x=130,y=370)

equal=Button(window,text="=",font="bold",bg="red",bd=8,fg="white",height="3",width="5",command=lambda:equalclick(),relief="raised").place(x=210,y=370)

plus=Button(window,text="+",font="bold",bg="red",bd=8,fg="white",height="3",width="5",command=lambda:btnclick("+"),relief="raised").place(x=290,y=370)


#--------------------------------------------------------------------------------------------------------------#
window.mainloop()
