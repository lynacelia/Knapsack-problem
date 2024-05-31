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
import time

values = df['values'].to_numpy()
weights = df['weights'].to_numpy()
n_items = len(df)
cap = df['capacity'].to_numpy()

def maximum(liste):
    maxi=liste[0]
    for i in liste:
        if i>=maxi:
            maxi= i
    return maxi

capacity=maximum(cap)

print('number of items in the dataset/knapsack = ',n_items)
print('capacity of the knapsack = ',capacity)
print('values of items:')
print(values)
print('weights of items:')
print(weights)

def evaluate(packing):
    '''
    Returns a list of [v,w], where v and w are the total value and weight of packing respectively

            Parameters:
                    packing (numpy array): numpy array of 1/0 to indicate a specified packing

            Returns:
            if  w > capacity:
            [w-capacity, w] (list):  (w-capacity) is total weight of packing minus the capacity
                                     w is the total weight of packing 
            else:
                    [v,w] (list):  v and w are the total value and weight of packing respectively
    '''   
    array = np.array(packing)
    values_array = np.array(values)
    weights_array = np.array(weights)
    # compute the total value of the items
    v = np.dot(array, values_array)  
    # compute the total weight of the items
    w = np.dot(array, weights_array)  
    if w > capacity:
        return [w-capacity, w]
    # returns array list of both total values and weight
    else:
        return [v, w]  # returns array list of both totarrayl varraylues arraynd totarrayl weight


def One_Flip_Neighbourhood(packing):
    '''
    Returns a list of of all neighbours in the Neighbourhood of packing

            Parameters:
                    packing (numpy array): numpy array of 1/0 to indicate a specified packing

            Returns:
                    neighbourhood (list): a list of of all neighbours in the Neighbourhood of packing
                    The size of the 1-flip neighborhood = 100 
    '''    
    neighbourhood = []
    for i in range(0, n_items):
        temp = list(packing)
        neighbourhood.append(temp)
        if neighbourhood[i][i] == 1:
            neighbourhood[i][i] = 0
        else:
            neighbourhood[i][i] = 1
    return neighbourhood

def Initial_solution(initial_proportion_items):  #initial prop of items is proportion of items in initial solution
    
    # seed
    np.random.seed(1)    
    # Draw samples from a binomial distribution
    packing = np.random.binomial(1, initial_proportion_items, size=n_items)
    print("Random Initial Solution of proportion: ", initial_proportion_items)
    print(np.array(packing))
    return packing

def Simulated_Annealing(initial_proportion_items, initial_temperature, iter_per_temperature, final_temperature):
    
    print("Simulated Annealing")
    print("Initial Proportion of items = ", initial_proportion_items)
    print("Initial temperature = ", initial_temperature)
    print("Final temperature = ", final_temperature)
    print("Number of Iterations per temperature = ", iter_per_temperature)
    # initialises no. of solutions checked
    solutions_checked = 0
    # initialises no. of improving moves
    total_improvements = 0   
    # initialises no. of random moves
    total_random_steps = 0   
    # packing_current holds the current solution
    packing_current = Initial_solution(initial_proportion_items) 
    # packing_best holds the best solution
    packing_best = packing_current[:]  
    # e_current holds the evaluation of the current soluton
    e_current = evaluate(packing_current)[:]  
    e_best = e_current[:]
    k = 0
    # checks the temperature
    while (initial_temperature/(k+1) > final_temperature):  
        # Counts number of iterations at current temperature
        j = 0     
        # Counts number of improvements at current iteration
        improvements = 0   
        # Count number of random steps at current iteration
        random_steps = 0    
        while (j < iter_per_temperature):
            solutions_checked += 1
            # creates a list of all neighbours in the neighbourhood of packing_current
            Neighbourhood = One_Flip_Neighbourhood(packing_current)
            # Selects random neighbour
            s = Neighbourhood[random.randint(0, len(Neighbourhood)-1)]   
            if (evaluate(s)[0] > e_current[0]):
                packing_current = s[:]
                e_current = evaluate(s)[:]
                improvements += 1
            else:
                delta = evaluate(packing_current)[0] - evaluate(s)[0]
                probability = random.uniform(0,1)
                randomness = math.exp(-1 * delta * (k+1) / (initial_temperature))
                if (probability < randomness):
                    packing_current = s[:]
                    e_current = evaluate(s)[:]
                    random_steps += 1
             # Records the best value found so far
            if(e_current[0] > e_best[0]):   
                packing_best = packing_current[:]
                e_best = e_current[:]
            j += 1
        # increase the total improvements
        total_improvements += improvements   
        # increase the total random steps
        total_random_steps += random_steps         
        k += 1
    print("Total number of random steps:", total_random_steps,"\n",
          "Total number of improvements:", total_improvements)
    print("Number of packings checked:", solutions_checked)
    p = np.array(packing_best)
    v = e_best[0]
    w = e_best[1]
    return p, v, w

def Tabu_Search(initial_proportion_items, tabu_tenure, max_super_best_steps):   
    
    print("Tabu Search")
    print("Initial Proportion of items = ", initial_proportion_items)
    print("Tabu tenure = ", tabu_tenure)
    print("Maximum super best steps = ", max_super_best_steps)
    # initialises no. of solutions checked
    solutions_checked = 0
    # packing_current holds the currentent solution
    packing_current = Initial_solution(initial_proportion_items)  
    # packing_best holds the best solution
    packing_best = packing_current[:]  
    # e_current holds the evaluation of the currentent soluton
    e_current = evaluate(packing_current)  
    # e_best holds the best solution in neighbourhood
    e_best = e_current[:] 
    # e_super_best holds the best solution so far
    e_super_best = e_current[:] 
    #  tabu_list holds the tabu status of each element in solution
    tabu_list = [0] * n_items   
    # counts the number of non-improving steps
    count = 0                     
    while (count < max_super_best_steps):
        # creates a list of all neighbours in the Neighbourhood of packing_current
        Neighbourhood = One_Flip_Neighbourhood(packing_current) 
        # initialises the number of element changed in current step
        neighbour = 0   
        # resets the best neighbour value to be zero
        e_best[0] = 0    
        # evaluates every member in the neighbourhood of packing_current
        for s in Neighbourhood:  
            solutions_checked += 1
            if (evaluate(s)[0] > e_best[0]) and (tabu_list[neighbour]==0):  
                # finds the best member and keep track of that solution
                packing_current = s[:]
                # e_best holds the best solution in neighbourhood
                e_best = evaluate(s)[:]  
                # neighbour selected at the current step
                neighbour_selected = neighbour   
            # updates the best solution found so far
            if (evaluate(s)[0] > e_super_best[0]):    
                packing_current = s[:]
                e_best = evaluate(s)[:]
                e_super_best = evaluate(s)[:]
                packing_super = s[:]
                neighbour_selected = neighbour
                change = 1
            neighbour += 1
        # counts the number of steps with the improvement
        count += 1   
        # Records the change status
        if(change == 1):            
            count = 0
            change = 0
        # Updates the tabu status of each item
        for i in range(0,len(tabu_list)-1):   
            tt = tabu_list[i]
            if(tt > 0):
                tabu_list[i] = tt - 1
        # updates the tabu status of selected items
        tabu_list[neighbour_selected] = tabu_tenure   
        print("Neighbour selected:", neighbour_selected, ", Best_value:", e_best[0])
        print("Highest total value found:", e_super_best[0])
        print("\n")
    print("Number of packings checked:", solutions_checked)
    p = np.array(packing_super)
    v = e_super_best[0]
    w = e_super_best[1]
    return p, v, w  


def run_SA(number_runs, initial_proportion_items, 
           initial_temperature, iter_per_temperature,  final_temperature):
  
    v_array = []
    w_array = []
    startsa=time.time()
    for i in range(number_runs):
        print('Number of runs of the algorithm =',i+1)
        print("\nStarting solve() ")
        packing, v, w = Simulated_Annealing(initial_proportion_items,
                                initial_temperature, iter_per_temperature, 
                                final_temperature)
        print("\nBest packing found: ")
        print(packing)
        print("\nTotal value of packing = %0.1f " % v)
        print("Total weight of packing = %0.1f " % w)
        v_array.append(v)
        w_array.append(w)

        with open('data/data1.csv', 'a+', newline="") as f:
                    f.write(f'{v}\n')
        
    endsa=time.time()
    tempssa=endsa-startsa
    print("++++++++++++++++++++++++++++++++",tempssa)
    with open('time1.csv', 'a+', newline="") as f: 
        f.write(f'{tempssa}\n')
    print("###################################End##########################################################")
    return v_array, w_array




def run_TS(number_runs, initial_proportion_items, 
           tabu_tenure, max_super_best_steps):

    
    v_array = []
    w_array = []
    startts=time.time()
    for i in range(number_runs):
        print('Number of runs of the algorithm =',i+1)
        print("\nStarting solve() ")
        packing, v, w = Tabu_Search(initial_proportion_items, 
                           tabu_tenure, max_super_best_steps)
        print("\nBest packing found: ")
        print(packing)
        print("\nTotal value of packing = %0.1f " % v)
        print("Total weight of packing = %0.1f " % w)
        v_array.append(v)
        w_array.append(w)

        with open('data/data2.csv', 'a+', newline="") as f:
                    f.write(f'{v}\n')        
  
    endts=time.time()
    tempsts=endts-startts
    print("++++++++++++++++++++++++++++++",tempsts) 
    with open('time2.csv', 'a+', newline="") as f: 
        f.write(f'{tempsts}\n')
    print("#####################################End########################################################")
    return v_array, w_array

def plot_value_weight(v_array, w_array, name_algo, number_runs):    
    '''
    Function to plot the total value of the items of the best packing in  each time of running the algorithm,
    and print average total value and weight in number_runs times of run

            Parameters:
                    v_array (list): a list to store total value of the items of the best packing in number_runs times of run
                    w_array (list): a list to store total weight of the items of the best packing in number_runs times of run
                    name_algo (str): the name of the algorithm, i.e either "Simulated Annealing" or "Tabu Search"
                    number_runs (int): number of times to run the algorithm
    '''
    avg_v_total = np.mean(v_array)
    avg_w_total = np.mean(w_array)
    print("\nAverage total value of packing in "+ str(number_runs) +" runs = %0.1f " % avg_v_total)
    print("\nAverage total weight of packing in "+ str(number_runs) +" runs = %0.1f " % avg_w_total)


number_runs = 1          
initial_proportion_items = Cooling_rate.get()
initial_temperature = initial_temperature.get()
iter_per_temperature = itera.get()
final_temperature = final_temperature.get()
name_algo = "Simulated Annealing"
v_array, w_array = run_SA(number_runs, initial_proportion_items, 
           initial_temperature, iter_per_temperature,  final_temperature)

plot_value_weight(v_array, w_array, name_algo, number_runs)



number_runs = 1              
initial_proportion_items = 0.1
tabu_tenure = tabutenure.get()
max_super_best_steps = maxsuper.get()
name_algo = "Tabu Search"
v_array, w_array = run_TS(number_runs, initial_proportion_items, 
           tabu_tenure, max_super_best_steps)

plot_value_weight(v_array, w_array, name_algo, number_runs)


muta, popu_size, cross_over, number_of_gen

solutions_per_pop = popu_size.get()
pop_size = (solutions_per_pop, n_items)
print('Population size = {}'.format(pop_size))
initial_population = np.random.randint(1, size = pop_size)
initial_population = initial_population.astype(int)
num_generations = number_of_gen.get()
print('Initial population: \n{}'.format(initial_population))

def cal_fitness(weights, values, population, capacity):
    fitness = np.empty(population.shape[0])
    for i in range(population.shape[0]):
        S1 = np.sum(population[i] * values)
        S2 = np.sum(population[i] * weights)
        if S2 <= capacity:
            fitness[i] = S1
        else :
            fitness[i] = 0 
    return fitness.astype(int) 

def selection(fitness, num_parents, population):
    fitness = list(fitness)
    parents = np.empty((num_parents, population.shape[1]))
    for i in range(num_parents):
        max_fitness_idx = np.where(fitness == np.max(fitness))
        parents[i,:] = population[max_fitness_idx[0][0], :]
        fitness[max_fitness_idx[0][0]] = -999999
    return parents

def crossover(parents, num_offsprings):
    offsprings = np.empty((num_offsprings, parents.shape[1]))
    crossover_point = int(parents.shape[1]/2)
    crossover_rate = cross_over.get()
    i=0
    while (parents.shape[0] < num_offsprings):
        parent1_index = i%parents.shape[0]
        parent2_index = (i+1)%parents.shape[0]
        x = rd.random()
        if x > crossover_rate:
            continue
        parent1_index = i%parents.shape[0]
        parent2_index = (i+1)%parents.shape[0]
        offsprings[i,0:crossover_point] = parents[parent1_index,0:crossover_point]
        offsprings[i,crossover_point:] = parents[parent2_index,crossover_point:]
        i=+1
    return offsprings 

def mutation(offsprings):
    mutants = np.empty((offsprings.shape))
    mutation_rate = muta.get()
    for i in range(mutants.shape[0]):
        random_values = rd.random()
        mutants[i,:] = offsprings[i,:]
        if random_values > mutation_rate:
            continue
        int_random_values = randint(0,offsprings.shape[1]-1)    
        if mutants[i,int_random_values] == 0 :
            mutants[i,int_random_values] = 1
        else :
            mutants[i,int_random_values] = 0
    return mutants



def optimize(weights, values, population, pop_size, num_generations, capacity):
    parameters, fitness_history = [], []
    num_parents = int(pop_size[0]/2)
    num_offsprings = pop_size[0] - num_parents 
    startga=time.time()
    for i in range(num_generations):
        fitness = cal_fitness(weights, values, population, capacity)
        fitness_history.append(fitness)
        parents = selection(fitness, num_parents, population)
        offsprings = crossover(parents, num_offsprings)
        mutants = mutation(offsprings)
        population[0:parents.shape[0], :] = parents
        population[parents.shape[0]:, :] = mutants
    endga=time.time()
    tempsga=endga-startga  
    print("++++++++++++++++",tempsga)  
    with open('time3.csv', 'a+', newline="") as f: 
        f.write(f'{tempsga}\n')

    print('Last generation: \n{}\n'.format(population)) 
    fitness_last_gen = cal_fitness(weights, values, population, capacity)      
    print('Fitness of the last generation: \n{}\n'.format(fitness_last_gen))
    max_fitness = np.where(fitness_last_gen == np.max(fitness_last_gen))
    
    #====================================================================
    fitnesssumdegen=np.sum(fitness_last_gen)
    print('le fitness maximum est :',np.max(fitnesssumdegen))

    fitnessmax=np.max(fitness_last_gen)
    print('le fitness min:',np.max(fitnessmax))


    with open('data/data4.csv', 'a+', newline="") as f: 
        f.write(f'{fitnessmax}\n')

    with open('data/data3.csv', 'a+', newline="") as f:
        f.write(f'{fitnesssumdegen}\n')

    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
    parameters.append(population[max_fitness[0][0],:])
    return parameters, fitness_history


parameters, fitness_history = optimize(weights, values, initial_population, pop_size, num_generations, capacity)
print('The optimized parameters for the given inputs are: \n{}'.format(parameters))







