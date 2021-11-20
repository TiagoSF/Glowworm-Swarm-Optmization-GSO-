
import random
import math
import matplotlib.pyplot as plt

def run(metodo):
    #G24
    if metodo == 1:
        
        bounds = [(0,3),(0,4)]
        nv = 2
        mm = -1
            
        #parametros
        particle_size = 100
        iterations = 200
        w = 0.9
        c1 = 1
        c2 = 1
         
        #FUNÇÃO G24
        def objective_function(O):
            x = O[0]
            y = O[1]
            r = 15
            nonlinear_constraint1 = -(2*x**4)+(8*x**3)-(8*x**2) + y - 2
            nonlinear_constraint2 = -(4*x**4)+(32*x**3)-(88*x**2)+(96*x) + y - 36
            
            
            if nonlinear_constraint1 > 0:
                penalty1 = 1
            else:
                penalty1 = 0
                
            if nonlinear_constraint2 > 0:
                penalty2 = 1
            else:
                penalty2 = 0
                
            z = -x-y + r*max(0,nonlinear_constraint1)**2 + r*max(0, nonlinear_constraint2)**2
            
            return z
        
    if metodo == 2:
        #FUNÇÃO G11
        def objective_function(O):
            x = O[0]
            y = O[1]
            r = 10
            linear_constraint1 = y-x**2
            y = x**2
            if linear_constraint1 > 0:
                penalty1 = 1
            else:
                penalty1 = 0
                
                
            z = (x**2)+((y-1)**2) + r*max(0,linear_constraint1)**2
            
            return z
        
        bounds = [(-1,1),(-1,1)]
        nv = 2
        mm = -1
        
        #parametros
        particle_size = 100
        iterations = 200
        w = 0.5
        c1 = 1
        c2 = 2
        
    if metodo == 3:
        #FUNÇÃO G13
        def objective_function(O):
            x  = O[0] 
            x2 = O[1] 
            x3 = O[1]
        
            
            r =0.045
            linear_constraint1 = (x**2)+((x2**2))+(x3**2)-25
            linear_constraint2 = 8*x + 14*x2+7*x3-56
                
            z = (1000-(x**2)-2*(x2**2)-(x3**2)-(x*x2)-(x*x3) + (r*max(0,linear_constraint1)**2) + r*max(0, linear_constraint2)**2)
            
            return z
        
        bounds = [(0,10),(0,10)]
        nv = 2
        mm = -1
        
        #parametros
        particle_size = 150
        iterations = 150
        w = 0.4
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
                self.valor = fitness_global_best_particle_position
                
            # print('result:')
            #print('Optimal solution:', global_best_particle_position)
            print('Objective function value:', fitness_global_best_particle_position)
            # plt.plot(A)
            # plt.title('Evolutionary process of the objective function value')
            # plt.xlabel('Iteration')
            # plt.ylabel('Objective Function')
            
    #------------------------------------
    if mm == -1:
        initial_fitness = float("inf")
    if mm == 1:
        initial_fitness = -float("inf")
    #------------------------------------
    
                
    out = PSO(objective_function,bounds,particle_size,iterations)
    return out.valor
                
                
                
