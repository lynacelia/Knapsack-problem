from cProfile import label
from cgitb import text
from os import curdir
from re import sub
from sqlite3 import Cursor, Row
from tkinter import *
from tkinter import font
from tkinter.font import ITALIC
from tkinter.simpledialog import SimpleDialog


from turtle import right, width
fenetre112 = Toplevel()
fenetre112.geometry('720x480')
fenetre112.title('Application')
fenetre112['bg']='#E1FFFA'
fenetre112.resizable(height=False, width=False)

##!!!!!!!!!!!!!!!!!!!!!!!!FONCTIONS!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


##!!!!!!!!!!!!!!!!!!!!!!FIN FONCTIONS!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


label_title = Label(
    fenetre112,
    text="Simulated annealing",
    font=("Courrier",30),
    bg=('#E1FFFA'),
    fg=("#00B39B") 
   )
label_title.place(x=20,y=20)

label=Label(
    fenetre112,
    text="Initial temperature",
    font=("Courrier",20),
    bg=('#E1FFFA'),
    fg=("#00B39B")
)
label.place(x=100, y=90)

initial_temperature=IntVar(value=100)
initialtemperature= Entry(
    fenetre112,
    textvariable=initial_temperature,
    insertwidth=2,
    justify=CENTER,
    font=("Courrier",15),
    borderwidth=4, 
    relief="groove",
    fg=("grey")
)
initialtemperature.place(x=400, y=90, width=80,height=40,)

label=Label(
    fenetre112,
    text="Final temperature",
    font=("Courrier",20),
    bg=('#E1FFFA'),
    fg=("#00B39B")
)
label.place(x=100, y=150)


final_temperature=IntVar(value=5)
finaltemperature= Entry(
    fenetre112,
    textvariable=final_temperature,
    insertwidth=2,
    justify=CENTER,
    font=("Courrier",15),
    borderwidth=4, 
    relief="groove",
    fg=("grey")
)
finaltemperature.place(x=400, y=150, width=80, height=40)

label=Label(
    fenetre112,
    text="Iteration of bearing",
    font=("Courrier",20),
    bg=('#E1FFFA'),
    fg=("#00B39B")
)
label.place(x=100, y=210)

itera=IntVar(value=50)
iteration= Entry(
    fenetre112,
    textvariable=itera,
    insertwidth=2,
    justify=CENTER,
    font=("Courrier",15),
    borderwidth=4, 
    relief="groove",
    fg=("grey")
)
iteration.place(x=400, y=210, width=80, height=40)

label=Label(
    fenetre112,
    text="Cooling rate",
    font=("Courrier",20),
    bg=('#E1FFFA'),
    fg=("#00B39B")
)
label.place(x=100, y=270)

Cooling_rate=DoubleVar(value=0.98)
Coolingrate= Entry(
    fenetre112,
    textvariable=Cooling_rate,
    insertwidth=2,
    justify=CENTER,
    font=("Courrier",15),
    borderwidth=4, 
    relief="groove",
    fg=("grey")
)
Coolingrate.place(x=400, y=270, width=80, height=40)


#*******************************GENETIQUE*************************************
##!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#*******************************GENETIQUE*************************************


Valider_button= Button (
    fenetre112,
    text="Validate",
    font=("Courrier",15),
    bg=('white'),
    fg=("#919695"),
    borderwidth=("4"),
    activebackground=("#00B39B"),
    activeforeground=("white"),
    cursor=("heart"),
   command= fenetre112.destroy
    ).place(x=550, y=340)  





if __name__ == "__main__":
    fenetre112.mainloop()