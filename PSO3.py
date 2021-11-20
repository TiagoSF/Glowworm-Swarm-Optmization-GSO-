# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 19:40:58 2020

@author: Tiago
"""


# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 17:35:57 2020

@author: Tiago
"""
import random
import time
import math
import matplotlib.pyplot as plt


#FUNÇÃO G13
def objective_function(O):
    x = O[0]
    x2 = O[1]
    x3 = O[2]
    x4 = O[3]
    x5 = O[4]
    
    nonlinear_constraint1 = (x**2)+(x2**2)+(x3**2)+(x4**2)+(x5**2)-10
    nonlinear_constraint2 = x2*x3 - 5*x4*x5
    nonlinear_constraint3 = (x**3)+(x2**3)+1
    
    if nonlinear_constraint1 > 0:
        penalty1 = 1
    else:
        penalty1 = 0
        
    if nonlinear_constraint2 > 0:
        penalty2 = 1
    else:
        penalty2 = 0
    if nonlinear_constraint3 > 0:
        penalty3 = 1
    else:
        penalty3 = 0
        
    z = math.exp(x*x2*x3*x4*x5) + penalty1 + penalty2 + penalty3
    
    return z

bounds = [(-2.3,2.3),(-2.3,2.3),(-3.2,3.2),(-3.2,3.2),(-3.2,3.2)]
nv = 5
mm = -1

#parametros
particle_size = 50
iterations = 100
w = 0.3
c1 = 1
c2 = 1

#--------------------------------------------
class Particle:
    def __init__(self,bounds):
        self.particle_position=[]
        self.particle_velocity=[]
        self.local_best_particle_position=[]
        self.fitness_local_best_particle_position = initial_fitness
        self.fitness_particle_position = initial_fitness
        
        for i in range(nv):
            self.particle_position.append(random.uniform(bounds[i][0], bounds[i][1]))
            self.particle_velocity.append(random.uniform(-1,1))
            
    def evaluate(self,objective_function):
        self.fitness_particle_position = objective_function(self.particle_position)
        if mm == -1:
            if self.fitness_particle_position < self.fitness_local_best_particle_position:
                self.local_best_particle_position = self.particle_position
                self.fitness_local_best_particle_position = self.fitness_particle_position
        if mm == 1:
            if self.fitness_particle_position > self.fitness_local_best_particle_position:
                self.local_best_particle_position=self.particle_position
                self.fitness_local_best_particle_position=self.fitness_particle_position
    
    def update_velocity(self,global_best_particle_position):
        for i in range(nv):
            r1 = random.random()
            r2 = random.random()
            
            cognitive_velocity = c1*r1*(self.local_best_particle_position[i] - self.particle_position[i])
            social_velocity = c2*r2*(global_best_particle_position[i] - self.particle_position[i])
            self.particle_velocity[i] = w*self.particle_velocity[i]+cognitive_velocity+social_velocity
            
    def update_position(self,bounds):
        for i in range(nv):
            self.particle_position[i] = self.particle_position[i]+self.particle_velocity[i]
            
            #check bounds
            if self.particle_position[i] > bounds[i][1]:
                self.particle_position[i]=bounds[i][1]
            if self.particle_position[i] < bounds[i][0]:
                self.particle_position[i]=bounds[i][0]

class PSO():
    def __init__(self, objective_function,bounds,particle_size, iterations):
        
        fitness_global_best_particle_position=initial_fitness
        global_best_particle_position=[]
        
        swarm_particle=[]
        for i in range(particle_size):
            swarm_particle.append(Particle(bounds))
        A=[]
        
        for i in range(iterations):
            for j in range(particle_size):
                swarm_particle[j].evaluate(objective_function)
                
                if mm == -1:
                    if swarm_particle[j].fitness_particle_position < fitness_global_best_particle_position:
                        global_best_particle_position = list(swarm_particle[j].particle_position)
                        fitness_global_best_particle_position = float(swarm_particle[j].fitness_particle_position)
                if mm == 1:
                    if swarm_particle[j].fitness_particle_position > fitness_global_best_particle_position:
                        global_best_particle_position = list(swarm_particle[j].particle_position)
                        fitness_global_best_particle_position = float(swarm_particle[j].fitness_particle_position)
            for j in range(particle_size):
                swarm_particle[j].update_velocity(global_best_particle_position)
                swarm_particle[j].update_position(bounds)
                
            A.append(fitness_global_best_particle_position)
            
        print('result:')
        print('Optimal solution:', global_best_particle_position)
        print('Objective function value:', fitness_global_best_particle_position)
        print('Evolutionary process of the objective function value:')
        plt.plot(A)
        plt.title('Evolutionary process of the objective function value')
        plt.xlabel('Iteration')
        plt.ylabel('Objective Function')
        
#------------------------------------
if mm == -1:
    initial_fitness = float("inf")
if mm == 1:
    initial_fitness = -float("inf")
#------------------------------------

            
PSO(objective_function,bounds,particle_size,iterations)
            
            
            