
from scipy.optimize import minimize
from scipy.optimize import differential_evolution
import math

def run(metodo):
    
    #--------------------------------------------------------------------
    def G11(O):
        x = O[0]
        y = O[1]
        r = 10
        linear_constraint1 = y-x**2
        y = x**2
                    
        z = (x**2)+((y-1)**2) + r*max(0,linear_constraint1)**2
                
        return z  

    #----------------------------------------------------------------------
    
    def G24(O):
        x = O[0]
        y = O[1]
        r = 15
        nonlinear_constraint1 = (-2*x**4)+(8*x**3)-(8*x**2)+y-2
        nonlinear_constraint2 = (-4*x**4)+(32*x**3)-(88*x**2)+(96*x)+y-(36)
                
                
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
    

    
    #-------------------------------------------------------------------------
    
    def G15(O):
        x  = O[0] 
        x2 = O[1]
        x3 = O[1]
    
        
        r =0.045
        linear_constraint1 = (x**2)+((x2**2))+(x3**2)-25
        linear_constraint2 = 8*x + 14*x2+7*x3-56
            
        z = (1000-(x**2)-2*(x2**2)-(x3**2)-(x*x2)-(x*x3) + (r*max(0,linear_constraint1)**2) + r*max(0, linear_constraint2)**2)
        
        return z

    #------------------------------------------------------------------------
    
    if metodo == 1:
        bounds = [(0,3),(0,4)]
        result = differential_evolution(G24, bounds)
        
    if metodo == 2:
        bounds = [(-1,1),(-1,1)]
        result = differential_evolution(G11, bounds)
        
    if metodo == 3:
        bounds = [(0,10),(0,10)]
        result = differential_evolution(G15, bounds)
        
    print(result.fun)
    return result.fun
























