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
fenetre113 = Toplevel()
fenetre113.geometry('720x480')
fenetre113.title('Application')
fenetre113['bg']='#E1FFFA'
fenetre113.resizable(height=False, width=False)

##!!!!!!!!!!!!!!!!!!!!!!!!FONCTIONS!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!



##!!!!!!!!!!!!!!!!!!!!!!FIN FONCTIONS!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

label_title = Label(
    fenetre113,
    text="Tabu search",
    font=("Courrier",30),
    bg=('#E1FFFA'),
    fg=("#00B39B") 
   )
label_title.place(x=20,y=20)



label=Label(
    fenetre113,
    text="Tabu tenure",
    font=("Courrier",20),
    bg=('#E1FFFA'),
    fg=("#00B39B")
)
label.place(x=100, y=150)


tabutenure=IntVar(value=30)
tabu_tenure= Entry(
    fenetre113,
    textvariable=tabutenure,
    insertwidth=2,
    justify=CENTER,
    font=("Courrier",15),
    borderwidth=4, 
    relief="groove",
    fg=("grey")
)
tabu_tenure.place(x=400, y=150, width=80, height=40)


label=Label(
    fenetre113,
    text="Max super Best steps",
    font=("Courrier",20),
    bg=('#E1FFFA'),
    fg=("#00B39B")
)
label.place(x=100, y=210)

maxsuper=IntVar(value=20)
max_super_best_steps= Entry(
    fenetre113,
    textvariable=maxsuper,
    insertwidth=2,
    justify=CENTER,
    font=("Courrier",15),
    borderwidth=4, 
    relief="groove",
    fg=("grey")
)
max_super_best_steps.place(x=400, y=210, width=80, height=40)

#*******************************GENETIQUE*************************************
##!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#*******************************GENETIQUE*************************************



Valider_button= Button (
    fenetre113,
    text="Validate",
    font=("Courrier",15),
    bg=('white'),
    fg=("#919695"),
    borderwidth=("4"),
    activebackground=("#00B39B"),
    activeforeground=("white"),
    cursor=("heart"),
    command= fenetre113.destroy
    ).place(x=550, y=340) 




if __name__ == "__main__":
    fenetre113.mainloop()