#calculator

from tkinter import *
expression = ""
 
 

def press(num):

    global expression
 
  
    expression = expression + str(num)
 
 
    equation.set(expression)
 
 

def equalpress():
 
 
    
    try: 
        global expression
 
       
        total = str(eval(expression))
 
        equation.set(total)
 
        expression = ""
 
    except:
 
        equation.set(" error ")
        expression = ""
 
 

def clear():
    global expression
    expression = ""
    equation.set("")

gui=Tk()


gui.configure(background="lavender")    
gui.title("AbhisheK's Calulator")
gui.geometry("350x350")

equation=StringVar()

Expression_Field=Entry(gui,textvariable=equation)

Expression_Field.grid(columnspan=4, ipadx=70)

button1 = Button(gui, text=' 1 ', fg='black', bg='orange',
                    command=lambda: press(1), height=1, width=7)
button1.grid(row=2, column=0)

button2 = Button(gui,text='2',fg='black',bg='orange',
                command=lambda:press(2),height=1,width=7)
button2.grid(row='2',column='1')

button3 = Button(gui,text='3',fg='black',bg='orange',
                command=lambda:press(3),height=1,width=7)
button3.grid(row='2',column='2')

button4 = Button(gui,text='4',fg='black',bg='orange',
                command=lambda:press(4),height=1,width=7)
button4.grid(row='2',column='3')

button5 = Button(gui,text='5',fg='black',bg='orange',
                command=lambda:press(5),height=1,width=7)
button5.grid(row='3',column='0')

button6 = Button(gui,text='6',fg='black',bg='orange',
                command=lambda:press(6),height=1,width=7)
button6.grid(row='3',column='1')

button7 = Button(gui,text='7',fg='black',bg='orange',
                command=lambda:press(7),height=1,width=7)
button7.grid(row='3',column='2')

button8 = Button(gui,text='8',fg='black',bg='orange',
                command=lambda:press(8),height=1,width=7)
button8.grid(row='3',column='3')

button9 = Button(gui,text='9',fg='black',bg='orange',
                command=lambda:press(9),height=1,width=7)
button9.grid(row='4',column='1')

button9 = Button(gui,text='0',fg='black',bg='orange',
                command=lambda:press(0),height=1,width=7)
button9.grid(row='4',column='2')

button10 = Button(gui,text='×',fg='red',bg='blue',
                command=lambda:press('*'),height=1,width=7)
button10.grid(row='5',column='0')

button11 = Button(gui,text='/',fg='red',bg='blue',
                command=lambda:press('/'),height=1,width=7)
button11.grid(row='5',column='1')

button12 = Button(gui,text='+',fg='red',bg='blue',
                command=lambda:press('+'),height=1,width=7)
button12.grid(row='5',column='2')

button13 = Button(gui,text='-',fg='red',bg='blue',
                command=lambda:press('-'),height=1,width=7)
button13.grid(row='5',column='3')

button14 = Button(gui,text='=',fg='red',bg='blue',
                command=lambda:press(''),height=1,width=7)
button14.grid(columnspan=8,ipadx=28)

gui.mainloop()