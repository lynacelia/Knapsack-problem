from cProfile import label
from cgitb import text
from os import curdir
from re import sub
from sqlite3 import Cursor, Row
from tkinter import *
from tkinter import font
from tkinter.font import ITALIC
from tkinter.simpledialog import SimpleDialog
import csv
import random as rd
from random import randint
from tkinter import filedialog
import sys
from tkinter import messagebox
import os


from turtle import right, title, width
fenetre12 = Tk()
fenetre12.geometry('720x480')
fenetre12.title('Application')
fenetre12['bg']='#E1FFFA'
fenetre12.resizable(height=False, width=False)



 #**************************FONCTIONS*********************************

header=["capacity" ,"weights" ,"values"]
def add():
    
    num=int(number_of_objects.get())
    capa=capacity.get()
   
    with open('knapsack6.csv', 'w', newline="") as f:

            writer= csv.writer(f,delimiter=",")
            writer.writerow(header)
            for i in range(num):
                writer.writerow([capa ,rd.randint(0,100) ,rd.randint(0,100)])
            
           
               
#*************************FIN FONCTIONS*************************
#**************************FONCTIONS*********************************
      

def chooseFile():
    os.startfile(r"C:\Users\ryham\Desktop\ANCIEN\Projet de fin d'études licence\finalpfe\knapsack9.csv")

#*************************FIN FONCTIONS*************************



label_title = Label(
    fenetre12,
    text="Benshmarks",
    font=("Courrier",24),
    bg=('#E1FFFA'),
    fg=("#00B39B") 
   )
label_title.place(x=20,y=10)

subtitle = Label(
    fenetre12,
    text="Enter your own benshmarks",
    font=("Courrier",15),
    bg=('#E1FFFA'),
    fg=("#00B39B") 
   )
subtitle.place(x=190,y=50)

#------------------------------caracteristiques------------------------------------
zone_dessin = Canvas(fenetre12,width=220,height=220,bg="white",bd=8)
zone_dessin.place(x=50, y=140)

title_caracteristics=Label(
    fenetre12,
    text="Caracteristics",
    font=("Courrier",20),
    bg=('WHITE'),
    fg=("#00B39B") 
)
title_caracteristics.place(x=50,y=100)

label=Label(
    fenetre12,
    text="Capacity",
    font=("Courrier",15),
    bg=('#E1FFFA'),
    fg=("#00B39B")
)
label.place(x=80, y=160)

capacity=IntVar(value=100)
Capacity= Entry(
    fenetre12,
    textvariable=capacity,
    insertwidth=2,
    justify=CENTER,
    font=("Courrier",15),
    borderwidth=4, 
    relief="groove",
    fg='gray'
   
)
Capacity.place(x=205, y=160, width=60)

label=Label(
    fenetre12,
    text="Number \n of objects",
    font=("Courrier",15),
    bg=('#E1FFFA'),
    fg=("#00B39B")
)
label.place(x=80, y=200)


number_of_objects=IntVar(value=4)
numberofobject= Entry(
    fenetre12,
    textvariable=number_of_objects,
    insertwidth=2,
    justify=CENTER,
    font=("Courrier",15),
    borderwidth=4, 
    relief="groove",
    fg='gray'
)
numberofobject.place(x=205, y=210, width=60)

label=Label(
    fenetre12,
    text="Name",
    font=("Courrier",15),
    bg=('#E1FFFA'),
    fg=("#00B39B")
)
label.place(x=80, y=265)


name_of_object=StringVar(value="Sac100x20")
nameofobject= Entry(
    fenetre12,
    textvariable=name_of_object,
    insertwidth=2,
    justify=CENTER,
    font=("Courrier",15),
    borderwidth=4, 
    relief="groove",
    fg='gray'
)
nameofobject.place(x=140, y=265, width=130)

#--------------------FIN caracteristique----------------------------------------
#-------------------------Objects-----------------------------------------------
zone_dessin = Canvas(fenetre12,width=290,height=220,bg="white",bd=8)
zone_dessin.place(x=360, y=140)

title_object=Label(
      fenetre12,
    text="Modification",
    font=("Courrier",20),
    bg=('WHITE'),
    fg=("#00B39B") 
)
title_object.place(x=360,y=100)




label=Label(
    fenetre12,
    text="Modify your own\n benshmarks",
    font=("Courrier",20),
    bg=('#E1FFFA'),
    fg=("#00B39B")
)
label.place(x=410, y=190)


CSV_button=Button (
    fenetre12,
    text="Modify now",
    font=("Courrier",15),
    bg=('white'),
    fg=("#919695"),
    borderwidth=("4"),
    activebackground=("#00B39B"),
    activeforeground=("white"),
    cursor=("heart"),
    command=chooseFile
    )
CSV_button.place(x=440, y=270, width=150)

#-------------------FIN object--------------------------------------

Retour_button=Button (
    fenetre12,
    text="Validate",
    font=("Courrier",15),
    bg=('white'),
    fg=("#919695"),
    borderwidth=("4"),
    activebackground=("#00B39B"),
    activeforeground=("white"),
    cursor=("heart"),
    command=fenetre12.quit
    )

Retour_button.place(x=620, y=400)


ADD_button=Button (
    fenetre12,
    text="Add randomly \nand Save",
    font=("Courrier",10),
    bg=('white'),
    fg=("#919695"),
    borderwidth=("4"),
    activebackground=("#00B39B"),
    activeforeground=("white"),
    cursor=("heart"),
    command=add
    )
ADD_button.place(x=120, y=310)


fenetre12.mainloop()