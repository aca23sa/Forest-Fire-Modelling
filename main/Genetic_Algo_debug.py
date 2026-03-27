from main.steps.in_pop import Initial_Pop
from main.steps.selection import Selection
from main.steps.crossover import Crossover
from main.steps.mutation import Mutation
from main.steps.insertion import Insertion

import time

class GeneticAlgo(object):
    def __init__(self):
        None
    def execute(self, mapp, iterations, selection, tournament, pop_size, parent_num, next_gen, cross, cross_prob, mut_method, mut_prob):

        # for fitness plot
    
        self.fitnesses = [] 
        self.runs = 0
        self.fittest = []
    
        "Initial Population"
    
        pop = Initial_Pop()
    
        population, self.coords = pop.initial_pop(mapp, population_size = pop_size)
        
        now = time.time()
        
        for k in range(1,iterations+1):
        
        
            "Selection"
        
            sel = Selection()
        
            scored, av_fitness = sel.score(population, self.coords)
        
            parents = sel.selection(scored = scored, num_parents = parent_num, tournament_size = tournament, selection_method = selection)
            
        
            "Crossover"
        
            next_gen = next_gen
        
            crossover = Crossover()
            offsprings_unmutated = crossover.crossover(cross_prob, parents, population, next_gen_size = next_gen, crossover_method = cross)
        
               
            "Mutation"
            mutation = Mutation()
        
            mutated_offsprings = mutation.mutate(offsprings = offsprings_unmutated, mutation_probability = mut_prob, mutation_method = mut_method)
            
            
            "Insertion"
        
            insertion = Insertion()
        
            population = insertion.insert(scored, population, next_gen, mutated_offsprings)
        
        
            scored, av_fitness = sel.score(population, self.coords)
            
            
            print("     Iteration: ", k, "       Av population fitness: ", av_fitness)
        
            # for plot
            self.runs += 1
            self.fitnesses.append(av_fitness)
            
            self.fittest.append(scored[0][1])
            
            print(" fittest: ", scored[0][0], scored[0][1])
            
            
            then = time.time()
            
            self.timing = then - now
            
            # stopping criterion #
            if k > 401: 
            
                diff = av_fitness - sum(self.fitnesses[k-400:k])/400
                perc = 0.01*av_fitness
                
                if diff < perc:
                
                    break
    
        # fittest tour to be plotted
        fittest_id=scored[0][0];
        print("fittest id ", scored[0][0])
        print(" final fittest: ", scored[0][1])
        for individual in population:
            if individual[0] ==fittest_id:
                fittest_tour=individual[1]
        self.fittest_tour = fittest_tour 
        print(" fittest tour: ", self.fittest_tour)
    
            
    
      
    def returnstuff(self):
        
        return self.fitnesses, self.runs, self.coords, self.fittest_tour, self.fittest, self.timing
        
