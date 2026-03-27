import operator
import random
import numpy as np

class Crossover(object):
    def __init__(self):
        None
    def crossover(self, crossover_probability, parents, in_population, next_gen_size,crossover_method = "one_point"):
        
        
        offsprings = []
        
                  
        route_dic = dict(in_population)
        par_dic = dict(parents)
        par_list = []
            
        for item in parents:
            par_list.append(item[0])
        
    
        # Number of offsprings produced
        #for i in range(1, next_gen_size +1):
        while len(offsprings) < next_gen_size:   
            
            # random choice between 1 0 (binomial)
            cross = np.random.choice((1,0), p=[crossover_probability, 1-crossover_probability])
            # For crossover probaility    
            if cross == 1:
            
                if crossover_method == "one_point":
            
                    "One-point crossover"
                                   
                    "CROSSOVER SET BY DEFAULT IN MIDPOINT"   
                    
                    # select two different parents from pool
                    two_parents = random.sample(par_list,2)
                    while two_parents[0] == two_parents[1]:
                        two_parents = random.sample(par_list,2)
        
                    parent_one_route = route_dic[two_parents[0]]
                
                    parent_two_route = route_dic[two_parents[1]]
                    
                    crossover_point = int(round(len(parent_one_route)))
            
                    offspring_l = parent_one_route[:crossover_point]
                        
                    offspring_r = parent_two_route[crossover_point:len(parent_one_route)]
         
                    offspring_1 = offspring_l + offspring_r
                    offspring_2 = parent_two_route[:crossover_point] + parent_one_route[crossover_point:len(parent_one_route)]
                    
                if crossover_method == "uniform":
                
                    "Uniform Crossover"
                    
                    # select two different parents
                    two_parents = random.sample(par_list, 2)
                    
                    while two_parents[0] == two_parents[1]:
                        two_parents = random.sample(par_list,2)
        
                    parent_one_route = route_dic[two_parents[0]]
                
                    parent_two_route = route_dic[two_parents[1]]
                    
                    offspring_1 = []
                    
                    offspring_2 = []
                    
                    for i in range(0, len(parent_one_route)):
                        if i % 2 == 0:
                            offspring_1.append(parent_two_route[i])
                            offspring_2.append(parent_one_route[i])
                            
                        else:
                            offspring_1.append(parent_one_route[i])
                            offspring_2.append(parent_two_route[i])
                            
                if crossover_method == "ordered":
                    
                    "Ordered Crossover (Two Point)"
                    
                    two_parents = random.sample(par_list, 2)
                    
                    while two_parents[0] == two_parents[1]:
                        two_parents = random.sample(par_list,2)
        
                    parent_one_route = route_dic[two_parents[0]]
                
                    parent_two_route = route_dic[two_parents[1]]
                    
                    cross_points = sorted(random.sample(range(1,len(parent_one_route)), 2))
                    
                    p1l = parent_one_route[:cross_points[0]]
                    p1r= parent_one_route[cross_points[1]:]
                    p1m = parent_one_route[cross_points[0]:cross_points[1]]
                    
                    p2l = parent_two_route[:cross_points[0]]
                    p2r= parent_two_route[cross_points[1]:]
                    p2m = parent_two_route[cross_points[0]:cross_points[1]]
                    
                    offspring_1 = p1l + p2m + p1r
                    offspring_2 = p2l + p1m + p2r
                    
                
            else: # If crossover is not applied parents are the same as offsprings
                
                two_parents = random.sample(par_list,2)
                while two_parents[0] == two_parents[1]:
                    two_parents = random.sample(par_list,2)
            
                parent_one_route = route_dic[two_parents[0]]
                
                parent_two_route = route_dic[two_parents[1]]
            
                offspring_1 = parent_one_route
                offspring_2 = parent_two_route
                   
                
            # check for offsprings that have duplicate cities or have sities missing
            if len(offspring_1) == len(set(offspring_1)):
                offsprings.append(offspring_1)   
            if len(offspring_2) == len(set(offspring_2)):
                offsprings.append(offspring_2)
            
        
        return offsprings
                
            
        