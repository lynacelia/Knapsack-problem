from cProfile import label
from cgitb import text
from lib2to3.pgen2.token import COMMA
from os import curdir
from re import sub
from sqlite3 import Cursor, Row
from tkinter import *
from tkinter import font
from tkinter.font import ITALIC
from tkinter.simpledialog import SimpleDialog
from tkinter import messagebox


from turtle import right, width
from webbrowser import get

from debugpy import listen
fenetre111 = Toplevel()
fenetre111.geometry('720x480')
fenetre111.title('Application')
fenetre111['bg']='#E1FFFA'
fenetre111.resizable(height=False, width=False)

##!!!!!!!!!!!!!!!!!!!!!!!!FONCTIONS!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!



##!!!!!!!!!!!!!!!!!!!!!!FIN FONCTIONS!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
##!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!



label_title = Label(
    fenetre111,
    text="Genetic solution",
    font=("Courrier",30),
    bg=('#E1FFFA'),
    fg=("#00B39B") 
   )
label_title.place(x=20,y=20)


label=Label(
    fenetre111,
    text="Population size",
    font=("Courrier",20),
    bg=('#E1FFFA'),
    fg=("#00B39B")
)
label.place(x=100, y=90)

popu_size=IntVar(value=500)
populationsize= Entry(
    fenetre111,
    textvariable= popu_size,
    insertwidth=2,
    justify=CENTER,
    font=("Courrier",15),
    borderwidth=4, 
    relief="groove",    
    fg=("grey")
)
populationsize.place(x=400, y=90, width=80,height=40,)

label=Label(
    fenetre111,
    text="Number of generations",
    font=("Courrier",20),
    bg=('#E1FFFA'),
    fg=("#00B39B")
)
label.place(x=100, y=150)


number_of_gen=IntVar(value=100)
numberofgen= Entry(
    fenetre111,
    textvariable=number_of_gen,
    insertwidth=2,
    justify=CENTER,
    font=("Courrier",15),
    borderwidth=4, 
    relief="groove",
    fg=("grey")
)
numberofgen.place(x=400, y=150, width=80, height=40)

label=Label(
    fenetre111,
    text="Mutation probability",
    font=("Courrier",20),
    bg=('#E1FFFA'),
    fg=("#00B39B")
)
label.place(x=100, y=210)

muta=DoubleVar(value=0.1)
Mutation= Entry(
    fenetre111,
    textvariable=muta,
    insertwidth=2,
    justify=CENTER,
    font=("Courrier",15),
    borderwidth=4, 
    relief="groove",
    fg=("grey")
)
Mutation.place(x=400, y=210, width=80, height=40)

label=Label(
    fenetre111,
    text="Cross-over probability",
    font=("Courrier",20),
    bg=('#E1FFFA'),
    fg=("#00B39B")
)
label.place(x=100, y=270)

cross_over=DoubleVar(value=0.99)
Cross_over= Entry(
    fenetre111,
    textvariable=cross_over,
    insertwidth=2,
    justify=CENTER,
    font=("Courrier",15),
    borderwidth=4, 
    relief="groove",
    fg=("grey")
)
Cross_over.place(x=400, y=270, width=80, height=40)

#*******************************GENETIQUE*************************************
##!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#*******************************GENETIQUE*************************************



Valider_button= Button (
    fenetre111,
    text="Validate",
    font=("Courrier",15),
    bg=('white'),
    fg=("#919695"),
    borderwidth=("4"),
    activebackground=("#00B39B"),
    activeforeground=("white"),
    cursor=("heart"),
    command= fenetre111.destroy
    ).place(x=550, y=340) 


 


if __name__ == "__main__":
    fenetre111.mainloop()

#*******************************GENETIQUE*************************************
##!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#*******************************GENETIQUE*************************************