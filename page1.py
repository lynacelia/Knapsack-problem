from cProfile import label
from cgitb import text
from tkinter import *
from tkinter.font import ITALIC

from turtle import right, width
import os
import sys
import csv
import  subprocess

 

fenetre = Tk()
fenetre.geometry('720x480')
fenetre.title('Problème du sac à dos')
fenetre.iconbitmap('res/icon1.ico')
fenetre['bg']='#E1FFFA'





##!!!!!!!!!!!!!!!!!!!!!!!!FONCTIONS!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


def gotopage11():
    
    fenetre11 = Toplevel()
    fenetre11.geometry('720x480')
    fenetre11.title('Problème du sac à dos')
    fenetre11.iconbitmap('res/icon1.ico')
    fenetre11['bg']='#E1FFFA'
    fenetre11.resizable(height=False, width=False)
    
    
    ##!!!!!!!!!!!!!!!!!!!!!!!!FONCTIONS!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    
    def gotopage1():
        fenetre11.destroy()
        import page1
    
    
    def callmain():
        os.system('python knapsack.py') 
           
    
    def gotopage111():
    
        fenetre = Toplevel()
        fenetre.geometry('720x480')
        fenetre.title('Problème du sac à dos')
        fenetre['bg']='#E1FFFA'
        fenetre.iconbitmap('res/icon1.ico')
        fenetre.resizable(height=False, width=False)
        
        ##!!!!!!!!!!!!!!!!!!!!!!!!FONCTIONS!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        
        
        
        #*******************************PAGE1111*************************************
        ##!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        #*******************************PAGE1111*************************************
        def gotopage1111():
            exec(open("./page1111.py").read())
            
        #*******************************PAGE1112*************************************
        ##!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        #*******************************PAGE1112*************************************
        def gotopage1112():
            exec(open("./page1112.py").read())

        
        #*******************************PAGE1113*************************************
        ##!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        #*******************************PAGE1113*************************************    
        def gotopage1113():
            exec(open("./page1113.py").read())
         
          
        
        ##!!!!!!!!!!!!!!!!!!!!!!FIN FONCTIONS!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        
        label_title = Label(
            fenetre,
            text="Choose you method:",
            font=("Courrier",35),
            bg=('#E1FFFA'),
            fg=("#008080") 
           )
        label_title.pack(expand=YES)
        
        yt_button=Button (
            fenetre,text="Genetic solution", 
            font=("Courrier",18),
            bg=('white'),
            fg=("#919695"),
            borderwidth=("4"),
            activebackground=("#008080"),
            activeforeground=("white"),
            cursor=("heart"),
            command=gotopage1111
            )
        
        yt1_button=Button (
            fenetre,
            text="Simulated annealing",
            font=("Courrier",18),
            bg=('white'),
            fg=("#919695"),
            borderwidth=("4"),
            activebackground=("#008080"),
            activeforeground=("white"),
            cursor=("heart"),
            command=gotopage1112
            )
        
        yt2_button=Button (
            fenetre,
            text="Tabu search",
            font=("Courrier",18),
            bg=('white'),
            fg=("#919695"),
            borderwidth=("4"),
            activebackground=("#008080"),
            activeforeground=("white"),
            cursor=("heart"),
            command=gotopage1113
            )
           
        
        yt_button.pack(pady=15)
        yt1_button.pack(pady=15)
        yt2_button.pack(pady=15)
        
        
        
        Valider_button=Button (
            fenetre,
            text="Validate",
            font=("Courrier",15),
            bg=('white'),
            fg=("#919695"),
            borderwidth=("4"),
            activebackground=("#008080"),
            activeforeground=("white"),
            cursor=("heart"),
            command=fenetre.destroy
            ).pack(side=RIGHT, padx=45, pady=25)
        
        
        fenetre.mainloop()
        
        #*******************************PAGE111*************************************
        ##!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        #*******************************PAGE111*************************************
        #*******************************PAGE111*************************************
        ##!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        #*******************************PAGE111*************************************
    
    def gotopage112():
        fenetrebensh = Toplevel()
        fenetrebensh.geometry('250x300')
        fenetrebensh.title('Problème du sac à dos')
        fenetrebensh.iconbitmap('res/icon1.ico')
        fenetrebensh['bg']='#E1FFFA'
        fenetrebensh.resizable(height=False, width=False)
        
        
        
        # --- functions ---
        
        def on_button():
            
            liste=[]
            print('les jeux selectionnés :')
            
            header=["listeselection"]
            with open('listeselection.csv', 'w', newline="") as f:
                writer= csv.writer(f,delimiter=",")
                writer.writerow(header)
                for i, var in enumerate(cb_vars):
                 if var.get():
                    liste.append(OPTIONS[i])
                    print(liste)
                for item in liste:
                     writer.writerow([item])

            
        fenetrebensh.destroy         
    
        
            
        
        
        # --- main ---

        OPTIONS = ["100x50","200x100","300x200","400x300",
        "500x400","600x500","700x600","800x700","New"]
        
        
        # --- Checkbuttons ---
        
        Label(fenetrebensh,
            text="Choose your benshmarks",
            font=("Courrier",12),
            bg=('#E1FFFA'),
            fg=("#919695"),
            borderwidth=("5"),
            activebackground=("#00B39B"),
            activeforeground=("white"),
            cursor=("heart")).pack(fill='x')
        
        cb_vars = []
        for x in OPTIONS:
            var = BooleanVar(value=False)
            cb_vars.append(var)
            
            c = Checkbutton(fenetrebensh, text=x, variable=var)
            c.pack()
        
        
        Button(fenetrebensh, text='VALIDATE', command=on_button).place(x=180, y=260)
        
        
        fenetrebensh.mainloop()
    
    
    def gotopage113():
        fenetrevisu = Toplevel()
        fenetrevisu.geometry('250x150')
        fenetrevisu.title('Problème du sac à dos')
        fenetrevisu.iconbitmap('res/icon1.ico')
        fenetrevisu['bg']='#E1FFFA'
        fenetrevisu.resizable(height=False, width=False)
        
        
        # --- functions ---
        
        def on_button():
            
            liste=[]
            print('The choosen graphs :')
            
            header=["graphe"]
            with open('grapheselect.csv', 'w', newline="") as f:
                writer= csv.writer(f,delimiter=",")
                writer.writerow(header)
                for i, var in enumerate(cb_vars):
                 if var.get():
                    liste.append(OPTIONS[i])
                    print(liste)
                for item in liste:
                     writer.writerow([item])
    
            os.system('python page114.py') 
            
        
        
        # --- main ---
        
        OPTIONS = ["Fitness","Execution time"]
        
        
        # --- Checkbuttons ---
        
        Label(fenetrevisu,
            text="Choose your graphs",
            font=("Courrier",12),
            bg=('#E1FFFA'),
            fg=("#919695"),
            borderwidth=("5"),
            activebackground=("#00B39B"),
            activeforeground=("white"),
            cursor=("heart")).pack(fill='x')
        
        cb_vars = []
        for x in OPTIONS:
            var = BooleanVar(value=False)
            cb_vars.append(var)
            
            c = Checkbutton(fenetrevisu, text=x, variable=var)
            c.pack()
        
        
            Button(fenetrevisu, text='VALIDER', command=on_button).place(x=150, y=80)
        
        
        
        fenetrevisu.mainloop()
    ##!!!!!!!!!!!!!!!!!!!!!!FIN FONCTIONS!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    
    label_title = Label(
    
        fenetre11,
        text="Experimentation:",
        font=("Courrier",40),
        bg=('#E1FFFA'),
        fg=("#008080") 
       )
    label_title.place(x=40, y=20)
    
    
    yt_button=Button (
        fenetre11,
        text="Settings",
        font=("Courrier",20),
        bg=('white'),
        fg=("#919695"),
        borderwidth=("4"),
        activebackground=("#008080"),
        activeforeground=("white"),
        cursor=("heart"),
        command=gotopage111
        )
    
    yt1_button=Button (
        fenetre11,
        text="Benshmarks",
        font=("Courrier",20),
        bg=('white'),
        fg=("#919695"),
        borderwidth=("4"),
        activebackground=("#008080"),
        activeforeground=("white"),
        cursor=("heart"),
        command=gotopage112
        )
    
    Lancer_button= Button (
        fenetre11,
        text="Launch",
        font=("Courrier",15),
        bg=('white'),
        fg=("#919695"),
        borderwidth=("4"),
        activebackground=("#008080"),
        activeforeground=("white"),
        cursor=("heart"),
        command=callmain
        ).place(x=550, y=270)
    
    Visualiser_button= Button (
        fenetre11,
        text="Visualisation",
        font=("Courrier",15),
        bg=('white'),
        fg=("#919695"),
        borderwidth=("4"),
        activebackground=("#008080"),
        activeforeground=("white"),
        cursor=("heart"),
        command=gotopage113
        ).place(x=550, y=320) 
    
    
   
    
    yt_button.place(x=120, y=160)
    yt1_button.place(x=320, y=160)
    
    
    fenetre11.mainloop()


def gotopage12():
    os.system('python page12.py')   

##!!!!!!!!!!!!!!!!!!!!!!FIN FONCTIONS!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

label_title = Label(
    fenetre,
    text="Problème du sac a dos",
    font=("Courrier",40),
    bg=('#E1FFFA'),
    fg=("#008080") 
   )
label_title.place(x=85, y=60)


Benshmarks=Button (
    fenetre,text="Benshmarks", 
    font=("Courrier",20),
    bg=('white'),
    fg=("#919695"),
    borderwidth=("3"),
    activebackground=("#008080"),
    activeforeground=("white"),
    cursor=("heart"),
    command=gotopage12
    )

Experimentation=Button (
    fenetre,
    text="Experimentation",
    font=("Courrier",20),
    bg=('white'),
    fg=("#919695"),
    borderwidth=("3"),
    activebackground=("#008080"),
    activeforeground=("white"),
    cursor=("heart"),
    command=gotopage11,
    )

Quitter=Button (
    fenetre,
    text="Cancel",
    font=("Courrier",15),
    bg=('white'),
    fg=("#919695"),
    borderwidth=("3"),
    activebackground=("#008080"),
    activeforeground=("white"),
    cursor=("heart"),
    command=fenetre.destroy
    )

Benshmarks.place(x=140, y=200)
Experimentation.place(x=360, y=200)
Quitter.place(x=570, y=350)


fenetre.mainloop()