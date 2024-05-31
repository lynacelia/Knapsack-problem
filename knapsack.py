from random import random
import random
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib 
matplotlib.rc('xtick', labelsize=15) 
matplotlib.rc('ytick', labelsize=15)


#**********************************************************************************
#**********************************************************************************
#**********************************************************************************

data = pd.read_csv("listeselection.csv")
data.columns = ["listeselection"]
liste = list(data.listeselection)

for i in range(len(liste)):

    if "100x50" in liste[i]:
        df = pd.read_csv('knapsack/knapsack1.csv')
        print(df)
        exec(open("./main.py").read()) 
    else: 
        if "200x100" in liste[i]:
            df = pd.read_csv('knapsack/knapsack2.csv')
            print(df)
            exec(open("./main.py").read())
            
        else: 
            if "300x200" in liste[i]:
                df = pd.read_csv('knapsack/knapsack3.csv')
                print(df)
                exec(open("./main.py").read())
                
            else: 
                if "400x300" in liste[i]:
                     df = pd.read_csv('knapsack/knapsack4.csv')
                     print(df)  
                     exec(open("./main.py").read())
                     
                else: 
                     if "500x400" in liste[i]:
                         df = pd.read_csv('knapsack/knapsack5.csv')
                         print(df)      
                         exec(open("./main.py").read()) 
                     else: 
                        if "600x500" in liste[i]:
                            df = pd.read_csv('knapsack/knapsack6.csv')
                            print(df)      
                            exec(open("./main.py").read()) 
                        else: 
                           if "700x600" in liste[i]:
                                df = pd.read_csv('knapsack/knapsack7.csv')
                                print(df)      
                                exec(open("./main.py").read()) 
                           else: 
                               if "800x700" in liste[i]:
                                    df = pd.read_csv('knapsack/knapsack8.csv')
                                    print(df)      
                                    exec(open("./main.py").read())
                               else:
                                   if "New" in liste[i]:
                                       df = pd.read_csv('knapsack/knapsack9.csv')
                                       print(df)      
                                       exec(open("./main.py").read()) 

                        
                           
                                    


