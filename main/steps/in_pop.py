import random

class Initial_Pop(object):
    
    def __init__(self):
        
        None
        
    def initial_pop(self, difficulty, population_size):
        
        # load problem
        x = open("main/csv_cities/" + str(difficulty) + ".csv", "r")

        self.coords = {}
    
        cit_name = 1
    
        # save coordinates of each city and give a unique id to each city
        for line in x:
            a = line.rstrip().split(",")
         
            if a == ['']:
                pass
            else:
                self.coords[cit_name] = [int(float(a[0])), int(float(a[1]))]
                
                cit_name += 1
                
        # define the cities in order
        cit_list = list(range(1,cit_name))
        
        # population list to be saved
        self.population = list()

        individual = 1
        
        # create the population by randomly shuffling the list of cities
        for i in range(0,population_size):
            self.population.append([individual,sorted(cit_list, key=lambda k: random.random())])
            individual += 1
            
        return self.population, self.coords
    
    
    
    
    
