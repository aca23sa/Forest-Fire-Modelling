import operator
import random

class Selection(object):
    def __init__(self):
        None
        
    def score(self,in_population, coords):
        
        
        score = {}
        
        av_fitness = 0
        
        # loop through every individual in the population
        for individual in in_population:
            temp_score = 0
            
            # obtain only the tour
            route = individual[1]
            
            # for every city in the tour
            for i in range(0,len(route)):
                
                #calculate the distance between the cities
                if i+1 < len(route):
                    
                    temp_score += ((coords[route[i+1]][0] - coords[route[i]][0])**2 + (coords[route[i+1]][1] - coords[route[i]][1])**2)**0.5
                    
                # close the loop    
                if i+1 == len(route):
                
                    temp_score += ((coords[route[0]][0] - coords[route[i]][0])**2 + (coords[route[0]][1] - coords[route[i]][1])**2)**0.5
            
            # save the score as the inverse of distance (fitness function)
            score[individual[0]] = 1/temp_score
            
            av_fitness+= 1/temp_score
        
        # store the fitnesses
        av_fitness = av_fitness/len(in_population)
        
        # sort the scores in descending order
        score = sorted(score.items(), key = operator.itemgetter(1), reverse=True)
                
        return score, av_fitness
    
    """""""Selection Operators"""""""
    
    "Tournament Selection"
    
    def selection(self, scored, num_parents, tournament_size = 10, selection_method = "Tournament_Selection"):
        
        if selection_method == "Tournament_Selection":
            
            # normalise fitnesses
            tot_fit = sum(dict(scored).values())
            normalised_dict = {k: v / tot_fit for k, v in dict(scored).items()}
        
            parents = []
            
            # to select individuals
            for i in range(1,num_parents+1):
                # sample individuals (as much as tournament size)
                sample = random.sample(normalised_dict.keys(), tournament_size)
            
                temp = {}
            
                for ind in sample:
                    temp[ind] = normalised_dict[ind]
                
                # sort tournament contestants and store highest fitness individual
                tour_winner = sorted(temp.items(), key = operator.itemgetter(1), reverse=True)[0]
            
                parents.append(tour_winner)
        
        
            return parents
    
        "Roulette Selection"
    
        # Enter Code Here
    
        "Elitism"
    
        if selection_method == "Elitism_Selection":
            
            # normalise fitnesses
            tot_fit = sum(dict(scored).values())
            normalised_dict = {k: v / tot_fit for k, v in dict(scored).items()}
            
            # sort fitnesses and keep fittest individuals
            parents = sorted(normalised_dict.items(), key=operator.itemgetter(1), reverse=True)[:num_parents]
        
            return parents
    
        "Rank-Based Selection"
        
        if selection_method == "Rank-Based_Selection":
            
            # normalise fitnesses
            tot_fit = sum(dict(scored).values())
            normalised_dict = {k: v / tot_fit for k, v in dict(scored).items()}
        
            # rank
            ranked = dict(enumerate(normalised_dict.keys(), 1))
        
            parents = []
        
            for i in range(1, num_parents+1):
            
                temp_sum = 0
                
                # where the point will land
                fixed_point = random.uniform(0, len(ranked)+1)
                
                # find where the point landed
                for index, key in ranked.items():
                
                    temp_sum += index
                
                    if temp_sum >= fixed_point:
                    
                        parents.append((key, normalised_dict[key]))
                    
                        break
                
            return parents
            
            
            