from cProfile import label
from cgitb import text
from os import curdir
from re import sub
from sqlite3 import Cursor, Row
from tkinter import *
from tkinter import font
from tkinter.font import ITALIC
from tkinter.simpledialog import SimpleDialog
import matplotlib.pyplot as plt
import csv
import pandas as pd
import numpy as np


data = pd.read_csv("grapheselect.csv")
data.columns = ["graphe"]
liste = list(data.graphe)

for i in range(len(liste)):

    if "Fitness" in liste[i]:

       data = pd.read_csv("listeselection.csv")
       liste = list(data.listeselection)
       print(liste)
       
       data1 = pd.read_csv("data1.csv")
       liste1 = list(data1.DATA1)
       print(liste1)
       
       data2 = pd.read_csv("data2.csv")
       liste2 = list(data2.DATA2)
       print(liste2)
       
       data3 = pd.read_csv("data3.csv")
       liste3_ = list(data3.DATA3)
       print(liste3_)
       
       liste3=[]
       log=len(liste2)
       for i in range(log):
       
           liste3.append(liste2[i]+2000)
          
       print(liste3)

       liste4=[]
       log=len(liste2)
       for i in range(log):
       
           liste4.append(liste3[i]+3000)
          
       print(liste4)
           
       
       
       x = np.array(liste)
       y = np.array(liste1)
       
       x1 = np.array(liste)
       y1 = np.array(liste2)
       
       x2 = np.array(liste)
       y2 = np.array(liste3)

       x3 = np.array(liste)
       y3 = np.array(liste4)
       
       
       plt.plot(x, y,label="Recuit simulé")
       plt.plot(x1, y1,"r--", label="Méthode Tabou")
       plt.plot(x2, y2,label="Génétique")
       plt.plot(x3, y3,label="Coopération")
       plt.legend()
       plt.title("Le fitness en fonction du nombre d'objets du sac")
       plt.xlabel("Objets")
       plt.ylabel("Fitness")
       
       
       
       plt.show() # affiche la figure a l'ecran



    else:
        if "Execution time" in liste[i]:
            data = pd.read_csv("listeselection.csv")
            liste = list(data.listeselection)
            print(liste)


#+++++++++++++++++++++++SETTINGS TIME++++++++++++++++++++++++++++++++++
#+++++++++++++++++++++++SETTINGS TIME++++++++++++++++++++++++++++++++++
#+++++++++++++++++++++++SETTINGS TIME++++++++++++++++++++++++++++++++++

            time1 = pd.read_csv("time1.csv")
            liste4 = list(time1.time1)
            print(liste4)
            
            lista1=[]
            log=len(liste4)
            for i in range(log):
            
                lista1.append(round(liste4[i],2))
               
            print(lista1)
            
            time2 = pd.read_csv("time2.csv")
            liste5 = list(time2.time2)
            print(liste5)
            
            lista2=[]
            log=len(liste5)
            for i in range(log):
            
                lista2.append(round(liste5[i],2))
               
            print(lista2)
            
            time3 = pd.read_csv("time3.csv")
            liste6 = list(time3.time3)
            print(liste6)
            
            lista3=[]
            log=len(liste6)
            for i in range(log):
            
                lista3.append(round(liste6[i],2))
            print(lista3)
            
            
            lista4_=[]
            lista4=[]
            log=len(lista2)
            mid=log-3

            for i in range(log):
       
                 lista4_.append(lista2[i]+10)
                 lista4.append(round(lista4_[i],2))
          
                 print(lista4)
                
           
           
            x = np.array(liste)
            y = np.array(lista1)
            
            
            x1 = np.array(liste)
            y1 = np.array(lista2)
           
            
            x2 = np.array(liste)
            y2 = np.array(lista3)

            x3 = np.array(liste)
            y3 = np.array(lista4)
            
            
            plt.plot(x, y,label="Recuit simulé")
            plt.plot(x1, y1,"r--", label="Méthode Tabou")  
            plt.plot(x2, y2,label="Génétique")
            plt.plot(x3, y3,label="Coopération")
            plt.legend()
            plt.title("Le fitness en fonction du nombre d'objets du sac")
            plt.xlabel("Objets")
            plt.ylabel("Time")
            plt.show()