from tkinter import *
from tkinter.font import Font


window=Tk()
window.geometry("500x500")
window.title("Calculator")
window.config(background='Dark Grey')
myfont=Font(family="Algerian", weight="bold", underline=True)
lab=Label(window,text="CALCULATOR", font=myfont, background="white")
lab.pack(side=TOP)
operator=''

textin: StringVar=StringVar()
operator=""

def press(number):
    global operator
    operator = operator + str(number)
    textin.set(operator)

def equalpress():
    global operator
    add: str=str(eval(operator))
    textin.set(add)
    operator=""

def equalpress():
    global operator
    sub: str=str(eval(operator))
    textin.set(sub)
    operator=""

def equalpress():
    global operator
    mul: str=str(eval(operator))
    textin.set(mul)
    operator=""

def equalpress():
    global operator
    div: str=str(eval(operator))
    textin.set(div)
    operator=''
def clear():
    global operator
    operator=""
    textin.set("")


metext=Entry(window,font=("Courier New", 12, 'bold'), textvariable=textin, width=25, bd=5, bg='powder blue')
metext.pack()

but1=Button(window,padx=14,pady=14,bd=4, command=lambda: press(1),text="1",font=("Courier New",13,'bold'))
but1.place(x=10,y=100)

but2=Button(window,padx=14,pady=14,bd=4, command=lambda: press(2),text="2",font=("Courier New",13,'bold'))
but2.place(x=10,y=170)

but3=Button(window,padx=14,pady=14,bd=4, command=lambda: press(3),text="3",font=("Courier New",13,'bold'))
but3.place(x=10,y=240)

but4=Button(window,padx=14,pady=14,bd=4, command=lambda: press(4),text="4",font=("Courier New",13,'bold'))
but4.place(x=75,y=100)

but5=Button(window,padx=14,pady=14,bd=4, command=lambda: press(5),text="5",font=("Courier New",13,'bold'))
but5.place(x=75,y=170)

but6=Button(window,padx=14,pady=14,bd=4, command=lambda: press(6),text="6",font=("Courier New",13,'bold'))
but6.place(x=75,y=240)

but7=Button(window,padx=14,pady=14,bd=4, command=lambda: press(7),text="7",font=("Courier New",13,'bold'))
but7.place(x=140,y=100)

but8=Button(window,padx=14,pady=14,bd=4, command=lambda: press(8),text="8",font=("Courier New",13,'bold'))
but8.place(x=140,y=170)

but9=Button(window,padx=14,pady=14,bd=4, command=lambda: press(9),text="9",font=("Courier New",13,'bold'))
but9.place(x=140,y=240)

butEqual=Button(window,padx=14,pady=14,bd=4, command=equalpress,text="=",font=("Courier New",13,'bold'))
butEqual.place(x=140,y=310)

but0=Button(window,padx=14,pady=14,bd=4, command=lambda: press(0),text="0",font=("Courier New",13,'bold'))
but0.place(x=10,y=310)

butdot=Button(window,padx=14,pady=14,bd=4, command=lambda: press("."),text=".",font=("Courier New",13,'bold'))
butdot.place(x=75,y=310)

butAdd=Button(window,padx=14,pady=14,bd=4, command=lambda: press("+"),text="+",font=("Courier New",13,'bold'))
butAdd.place(x=205,y=100)

butSub=Button(window,padx=14,pady=14,bd=4, command=lambda: press("-"),text="-",font=("Courier New",13,'bold'))
butSub.place(x=205,y=170)

butMul=Button(window,padx=14,pady=14,bd=4, command=lambda: press("*"),text="*",font=("Courier New",13,'bold'))
butMul.place(x=205,y=240)

butDiv=Button(window,padx=14,pady=14,bd=4, command=lambda: press("/"),text="/",font=("Courier New",13,'bold'))
butDiv.place(x=205,y=310)

butClear=Button(window,padx=14,pady=14,bd=4, command=clear,text="CE",font=("Courier New",13,'bold'))
butClear.place(x=270,y=100)

window.mainloop()

