import operator
import random
import numpy as np

class Mutation(object):
    def __init__(self):
        None
    def mutate(self, offsprings, mutation_probability,mutation_method = "TWORS"):
        new_gen = []
        
            
        for item in offsprings:
            
            cross = np.random.choice((1,0), p=[mutation_probability, 1-mutation_probability])
            
            if cross == 1:
                
                if mutation_method == "TWORS":
                    
                    temp = []
            
                    ' Note on the mutation points to be exchanges/swapped'
                    # The following line of code can be set to be fixed by an array
                    # I introduced the randomness since i think it will help 
                    # because we have to many duplicated
                    mutation_point = random.sample(range(0,len(item)), 2) 
                    #print("mutation ", item)
                    
                    

                    for i in range(0, len(item)):
                        if i == mutation_point[1]:
                            temp.append(item[mutation_point[0]])
                        if i == mutation_point[0]:
                            temp.append(item[mutation_point[1]])
                        else:
                            temp.append(item[i])

                    del temp[mutation_point[1]+1]
                
                    new_gen.append(temp)
                    
                if mutation_method =="CIM":
                    
                    temp = []
                    
                    #mutation_point = random.randint(1, len(item)-1)
                    mutation_point = round(len(item))

                    a = item[:mutation_point]
                    b = item[mutation_point:]
                    
                    temp = list(reversed(a)) + list(reversed(b))
                    
                    new_gen.append(temp)
                    
                if mutation_method == "RSM":
                    
                    temp = []
                    
                    mutation_point = sorted(random.sample(range(1,len(item)), 2)) 
                    
                    a = item[:mutation_point[0]]
                    b = item[mutation_point[1]:]
                    c = list(reversed(item[mutation_point[0]:mutation_point[1]]))
                    
                    temp = a + c + b
                    
                    new_gen.append(temp)
            else:
                
                new_gen.append(item)
                
        return new_gen
                    
                    
                
                
                