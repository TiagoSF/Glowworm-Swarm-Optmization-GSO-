


import random
import time
import math
import matplotlib.pyplot as plt

def run(metodo):
    if metodo == 2:
    #-----------------------------------------------------------------------------
        ##FUNÇÃO G11
        def objective_function(x,y):
            r = 10
            linear_constraint1 = (y-x**2)
            y = x**2
            
            # if linear_constraint1 > 0:
            #     penalty1 = 1
            # else:
            #     penalty1 = 0
                
                
            z = ((x**2)+((y-1)**2) + r*max(0,linear_constraint1)**2)
            
            return z
        
        
        
        # #parametros
        particle_size = 5
        iterations = 1000
        rho = 0.5
        gamma = 0.5         #Luciferin enhancement constant
        s = 0.03            #step size
        beta = 0.08         #decision range gain
        n_t = 3             #Desired no. of neighbors
        l_0 = 100          #valor inicial de luciferin
        r_s = 10            #Sensor range
        r_0 = 0.2           #Luciferin decay constant
        
        lower_boundX = -1
        upper_boundX = 1
        lower_boundY = -1
        upper_boundY = 1
    #-----------------------------------------------------------------------------
    
    #-----------------------------------------------------------------------------
    if metodo == 1:
    # #FUNÇÃO G24
        def objective_function(x,y):
            r = 15
            
            nonlinear_constraint1 = (-(2*x**4)+(8*x**3)-(8*x**2) + y - 2)
            nonlinear_constraint2 = (-(4*x**4)+(32*x**3)-(88*x**2)+(96*x) + y - 36)
            
            
                
            z = (-x-y + r*max(0,nonlinear_constraint1)**2 + r*max(0, nonlinear_constraint2)**2 )
            
            return z
        
        particle_size = 5
        iterations = 10000
        rho = 0.8
        gamma = 0.6         #Luciferin enhancement constant
        s = 0.04            #step size
        beta = 0.08         #decision range gain
        n_t = 2            #Desired no. of neighbors
        l_0 = 80           #valor inicial de luciferin
        r_s = 15            #Sensor range
        r_0 = 0.3           #Luciferin decay constant
        
        lower_boundX = 0
        upper_boundX = 3
        lower_boundY = 0
        upper_boundY = 4
    #-----------------------------------------------------------------------------
    #G13
    if metodo == 3:
        def objective_function(x,y):
             x  = x 
             x2 = y 
             x3 = y 
        
            
             r =0.045
             linear_constraint1 = (x**2)+((x2**2))+(x3**2)-25
             linear_constraint2 = 8*x + 14*x2+7*x3-56
                
             z = (1000-(x**2)-2*(x2**2)-(x3**2)-(x*x2)-(x*x3) + (r*max(0,linear_constraint1)**2) + r*max(0, linear_constraint2)**2)
            
             return z
   
        
        particle_size = 5
        iterations = 1000
        rho = 0.9
        gamma = 0.6         #Luciferin enhancement constant
        s = 0.03            #step size
        beta = 0.05         #decision range gain
        n_t =5             #Desired no. of neighbors
        l_0 = 100            #valor inicial de luciferin
        r_s = 10           #Sensor range
        r_0 = 0.6           #Luciferin decay constant
        
        lower_boundX = 0
        upper_boundX = 10
        lower_boundY = 0
        upper_boundY = 10
    #-----------------------------------------------------------------------------------------  
    
    class Glowworms(object):
        def __init__(self, l_0,posX,posY,r_0):
            self.luciferin = l_0
            self.posX = posX
            self.posY = posY
            self.r_0 = r_0
    
    glowworms = []
    
    def initialize():
        for i in range(particle_size):
            # posX = random.randint(lower_boundX,upper_boundX) #bounds
            # posY = random.randint(lower_boundY,upper_boundY) #bounds
            posX = random.uniform(lower_boundX,upper_boundX) #bounds
            posY = random.uniform(lower_boundY,upper_boundY) #bounds
            
            glowworms.append(Glowworms(l_0, posX, posY, r_0))
            
            
    
    def distancia(i,j):
        return math.sqrt(((j.posX - i.posX)**2) + ((j.posY - i.posY)**2))  
            
    def getNeighborhood(i, glowworms):
        neighborhood = []
        for j in glowworms:
            if (distancia(i,j) < i.r_0) and (i.luciferin < j.luciferin):
                neighborhood.append(j)
        return neighborhood
    
    def sumLuciferin(neighborhood):
        soma = 0
        for i in neighborhood:
            soma = soma + i.luciferin
        return soma
    
    def rouletteSelect(weight):
        weight_sum = 0
        for i in range(len(weight)):
            weight_sum += weight[i]
        
        value = random.uniform(0, 1)*weight_sum
        
        for i in range(len(weight)):
            value -= weight[i]
            if value<=0:
                return i
            
        return len(weight)-1
            
    
    def selectGlowworm(neighborhood, probabilidades):
        index = rouletteSelect(probabilidades)
        
        if len(neighborhood) > 0:
            return neighborhood[index]
        
        return 0
    
    def euclideanNorm(x, y):
        dist =  abs(math.sqrt((x**2)+(y**2)))
        if dist == 0:
            return 1
        return dist
            
            
    def step(glowworms):
        
        for t in range(iterations):
            #update luciferin
            for i in glowworms:
                i.luciferin = (1-rho)*i.luciferin - gamma*objective_function(i.posX, i.posY)
                #maximização
                #i.luciferin = (1-rho)*i.luciferin + gamma*objective_function(i.posX, i.posY)
            
            
            #MOVEMENT
            for i in glowworms:
                neighborhood = getNeighborhood(i, glowworms)
                liciferinSumOfNeighborhood = sumLuciferin(neighborhood)
                probabilidades = []
                
                for c in range(len(neighborhood)):
                    j = neighborhood[c]
                    probabilidade = (j.luciferin - i.luciferin)/(liciferinSumOfNeighborhood - i.luciferin)
                    probabilidades.append(probabilidade)
                j = selectGlowworm(neighborhood,probabilidades)
                
                if j != 0:
                    oldIPosX = i.posX
                    oldIPosY = i.posY
                    
                    oldJPosX = j.posX
                    oldJPosY = j.posY
                    
                    i.posX = oldIPosX + s*((oldJPosX - oldIPosX) / (euclideanNorm(oldJPosX - oldIPosX, oldJPosY - oldIPosY)));
                    i.posY = oldIPosY + s*((oldJPosY - oldIPosY) / (euclideanNorm(oldJPosX - oldIPosX, oldJPosY - oldIPosY)));
                    
                    if i.posX> upper_boundX:
                        i.posX = upper_boundX
                    if i.posX< lower_boundX:
                        i.posX = lower_boundX
                    if i.posY> upper_boundY:
                        i.posY = upper_boundY
                    if i.posY < lower_boundY:
                        i.posY = lower_boundY
                    
                    
                i.r_0 = min(r_s, max(0, i.r_0 + beta*(n_t - len(neighborhood))) )
                
                
    
    initialize()
    
    step(glowworms)
    
    resultados = []
    
    for i in glowworms:
        resultados.append(objective_function(i.posX, i.posY))
    
    print("fitness:", resultados)
    return resultados

        
        
        
        
        
        
        
        
            
