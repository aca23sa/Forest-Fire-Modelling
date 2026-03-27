import operator
import random
import numpy as np

class Insertion(object):
    def __init__(self):
        None
    def insert(self, scored, population, next_gen_size, mutated_offsprings):
        # sort individuals from previous gen 
        sorted_pop = []
        
        #iter = len(mutated_offsprings)
        
        for i in range(0,len(scored)):
            sorted_pop.append(population[scored[i][0]-1])
        
        # cut of the lowest ranked 50 individuals from previous gen
        survived = sorted_pop[:len(sorted_pop)-next_gen_size]
        
        # replace those individuals with fitter version
    
        
        # survived individuals (by index) 
        survived_ind = []
        
        for l in range(0,len(survived)):
            survived_ind.append(survived[l][0])
        
        #print(survived_ind)
        # lost individuals (numbers to go on new _gen)
        lost_ind = []
        
        setaki = list(range(1,len(population) + 1))
        
        if len(mutated_offsprings) == len(population):
            
            lost_ind = list(range(1,len(population) + 1))
            
        else:
            
            for item in setaki:
                if item not in survived_ind:
                    lost_ind.append(item)
                
        # add the indices to the mutated routed
        mutated = []
    
        for j in range(0, len(mutated_offsprings)):
            
            mutated.append([lost_ind[j], mutated_offsprings[j]])
            
        population = survived + mutated
        
        return population