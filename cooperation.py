from random import random
import random
import math
from matplotlib.cbook import violin_stats
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib 
matplotlib.rc('xtick', labelsize=15) 
matplotlib.rc('ytick', labelsize=15)
import numpy as np
import pandas as pd
import random as rd
from random import randint
import matplotlib.pyplot as plt
from page1111 import muta, popu_size, cross_over, number_of_gen
from page1112 import Cooling_rate, itera, final_temperature, initial_temperature
from page1113 import maxsuper, tabutenure
import csv

if __name__ == "__main__":
    print("Nastavte parametre algoritmov v programe.")
    while True:
        vstup, cities, metoda = load_input()
        if cities is None:
            print("Zly vstup :)")
            continue
def GeneticAlgorithm():
  
        if metoda.lower() == "vsetky":
            with ProcessPoolExecutor(max_workers=3) as executor:
                riesenie_GA = executor.submit(GeneticAlgorithm, cities, genetic_algorithm_args)
                riesenie_SA = executor.submit(SimulatedAnnealing, cities, simulated_annealing_args)
                riesenie_TABU = executor.submit(TabuSearch, cities, tabu_search_args)
            print_riesenie(riesenie_GA.result(), vstup)
            print_riesenie(riesenie_SA.result(), vstup)
            print_riesenie(riesenie_TABU.result(), vstup)

        elif metoda.lower() == "ga":
            riesenie_GA = GeneticAlgorithm(cities, genetic_algorithm_args)
            print_riesenie(riesenie_GA, vstup)
        elif metoda.lower() == "sa":
            riesenie_SA = SimulatedAnnealing(cities, simulated_annealing_args)
            print_riesenie(riesenie_SA, vstup)
        elif metoda.lower() == "tabu":
            riesenie_TABU = TabuSearch(cities, tabu_search_args)
            print_riesenie(riesenie_TABU, vstup)
# first menu of the application
def initialMenu():
  print("------------------------------------------------")
  print()
  print("               STREAMING VIDEOS                 ")
  print()
  print("                          by Trio de Informática")
  print()
  input("Press a key to start ")
  print()
  print("------------------------------------------------")

# menu to choose the file to get the input
# it's ordered by file size
def fileOptions():
  print("------------------------------------------------")
  print()
  print("Choose the input file: ")
  print()
  print("1: Small")
  print("2: Me at the Zoo")
  print("3: VWS Small")
  print("4: Videos Worth Spreading")
  print("5: Trending Today")
  print("6: Kittens")
  print()
  while True:
    optionStr = input("Option: ")
    option = int(optionStr)
    if option == 1:
      file = "src/input/small.in"
      break
    elif option == 2:
      file = "src/input/me_at_the_zoo.in"
      break
    elif option == 3:
      file = "src/input/vws_verysmaller.in"
      break
    elif option == 4:
      file = "src/input/videos_worth_spreading.in"
      break
    elif option == 5: 
      file = "src/input/trending_today.in"
      break
    elif option == 6: 
      file = "src/input/kittens.in"
      break
    else: 
      print("Invalid input: Try again!")
      continue
  print("------------------------------------------------")
  return file, option

# menu to choose the algorithm to run
def algorithmOptions(file, fileSize):
  print("------------------------------------------------")
  print()
  print("Choose the algorithm: ")
  print()
  print("1: Hill Climbing")
  print("2: Simulated Annealing")
  print("3: Genetic - Steady State")
  print("4: Genetic - Generational")
  print("5: Iterative Local Search")
  print("6: Guided Local Search")
  print("7: Tabu Search")
  print()
  
  while True:
    optionStr = input("Option: ")
    option = int(optionStr)
    if option == 2:
      simulatedAnnealingMenu()
      break
    elif option == 3:
      geneticSteadyStateMenu( fileSize)
      break
    elif option == 4: 
      geneticGenerationalMenu( fileSize)
      break
    elif option == 5: 
      iterativeLocalSearchMenu(fileSize)
      break
    elif option == 6:
      guidedLocalSearchMenu()
      break
    elif option == 7:
      tabuSearchMenu()
      break
    else: 
      print("Invalid input: Try again!")
      continue


def simulatedAnnealing():
  print("------------------------------------------------")
  print()
  print("              SIMULATED ANNEALING               ")
  print()
# menu to run the simulated annealing algorithm
def simulatedAnnealingMenu(data):
  print("------------------------------------------------")
  print()
  print("              SIMULATED ANNEALING               ")
  print()
  sol, time = simulatedAnnealing(data)

  print("------------------------------------------------")



  print("------------------------------------------------")
def generationalGenetic():
  print("------------------------------------------------")
  print()
  print("             GENETIC              ")
  print()
#menu to run the genetic generational algorithm
def geneticGenerationalMenu(data, fileSize):
  print("------------------------------------------------")
  print()
  print("             GENETIC                ")
  print()
  sol, time = generationalGenetic(data, 50, 15, 0.3)
  print("------------------------------------------------")

#menu to run the tabu search algorithm
def tabuSearchMenu(data):
  print("------------------------------------------------")
  print()
  print("                  TABU SEARCH                   ")
  print()
  sol, time = tabuSearchStatic(data,10)
  print("------------------------------------------------")



initialMenu()
file, size = fileOptions()
algorithmOptions(file, size)