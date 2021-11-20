
import numpy as np
from scipy.stats import f_oneway
import statistics
from statsmodels.stats.multicomp import (pairwise_tukeyhsd,MultiComparison)
import PSO
import DE
import glowworm_opt
import math
import random
import time
import matplotlib.pyplot as plt

#metodo = 1 - G24
bestvalueG24 = -5.5080
#metodo = 2 - G11
bestvalueG11 = 0.7499
#metodo = 3 - G13
bestvalueG15 = 961.7150

#--------------------------------------------------------------------------------------------
metodo = 1 
outPSO1 = [] #erro
#saidas para metodo 1
for i in range(0,5):
    out = (PSO.run(metodo)-bestvalueG24)
    outPSO1.append(abs(out))

#print('erro absoluto 1:', outPSO1)

metodo = 2
outPSO2 = [] #erro
#saidas para metodo 2
for i in range(0,5):
    out = (PSO.run(metodo)-bestvalueG11)
    outPSO2.append(abs(out))

#print('erro absoluto 2:', outPSO2)

metodo = 3
outPSO3 = [] #erro
#saidas para metodo 3
for i in range(0,5):
    out = (PSO.run(metodo)-bestvalueG15)
    outPSO3.append(abs(out))

#print('erro absoluto PSO para G15:', outPSO3)


#one way anova
anova_PSO = f_oneway(outPSO1, outPSO2, outPSO3)
print('ANOVA para PSO:', anova_PSO)
v = np.concatenate([outPSO1, outPSO2, outPSO3])
labels = ['outPSO1']*len(outPSO1)+['outPSO2']*len(outPSO2)+['outPSO3']*len(outPSO3)
tukey_results_PSO = pairwise_tukeyhsd(v, labels, 0.05)
print('Teste Tukey para PSO:', tukey_results_PSO)
#-----------------------------------------------------------------------------------------------


metodo = 1 
outDE1 = [] #erro
#saidas para metodo 1
for i in range(0,5):
    out = DE.run(metodo)-bestvalueG24
    outDE1.append(abs(out))

#print('erro absoluto DE para G24:', outDE1)

metodo = 2
outDE2 = [] #erro
#saidas para metodo 2
for i in range(0,5):
    out = DE.run(metodo)-bestvalueG11
    outDE2.append(abs(out))

#print('erro absolutoDE para G11:', outDE2)

metodo = 3
outDE3 = [] #erro
#saidas para metodo 3
for i in range(0,5):
    out = DE.run(metodo)-bestvalueG15
    outDE3.append(abs(out))

#print('erro absoluto DE para G15:', outDE3)


#one way anova
anova_DE = f_oneway(outDE1, outDE2, outDE3)
print('ANOVA para DE:', anova_DE)
v = np.concatenate([outDE1, outDE2, outDE3])
labels = ['outDE1']*len(outDE1)+['outDE2']*len(outDE2)+['outDE3']*len(outDE3)
tukey_results_DE = pairwise_tukeyhsd(v, labels, 0.05)
print('Teste Tukey para DE:', tukey_results_DE)
#---------------------------------------------------------------------------------------------------


metodo = 1 
outGW1 = [] #erro
#saidas para metodo 1
out = glowworm_opt.run(metodo)
for i in range(len(out)):
    outGW1.append(abs(out[i]-bestvalueG24))

#print('erro absoluto 1:', outGW1)


metodo = 2
outGW2 = [] #erro
#saidas para metodo 2
out = glowworm_opt.run(metodo)
for i in range(len(out)):
    outGW2.append(abs(out[i]-bestvalueG11))

#print('erro absoluto 2:', outGW2)


metodo = 3
outGW3 = [] #erro
#saidas para metodo 3

out = glowworm_opt.run(metodo)
for i in range(len(out)):
    outGW3.append(abs(out[i]-bestvalueG15))

#print('erro absoluto 3:', outGW3)


#one way anova
anova_GW = f_oneway(outGW1, outGW2, outGW3)
print('ANOVA para Glowworm:', anova_GW)

v = np.concatenate([outGW1, outGW2, outGW3])
labels = ['outGW1']*len(outGW1)+['outGW2']*len(outGW2)+['outGW3']*len(outGW3)
tukey_results_GW = pairwise_tukeyhsd(v, labels, 0.05)
print('Teste Tukey para GW:', tukey_results_GW)


# #------------------------------------------------------------------------------

anova_G24 = f_oneway(outGW1, outPSO1, outDE1)
print("\nANOVA entre os metodos, para G24", anova_G24)
anova_G11 = f_oneway(outGW2, outPSO2, outDE2)
print("ANOVA entre os metodos, para G11", anova_G11)
anova_G15 = f_oneway(outGW3, outPSO3, outDE3)
print("ANOVA entre os metodos para G15", anova_G15,"\n")


v = np.concatenate([outGW1, outPSO1, outDE1])
labels = ['outGW1']*len(outGW1)+['outPSO1']*len(outPSO1)+['outDE1']*len(outDE1)
tukey_results_G24 = pairwise_tukeyhsd(v, labels, 0.05)
print('Teste Tukey para G24:', tukey_results_G24)

v = np.concatenate([outGW2, outPSO2, outDE2])
labels = ['outGW2']*len(outGW2)+['outPSO2']*len(outPSO2)+['outDE2']*len(outDE2)
tukey_results_G11 = pairwise_tukeyhsd(v, labels, 0.05)
print('Teste Tukey para G11:', tukey_results_G11)

v = np.concatenate([outGW3, outPSO3, outDE3])
labels = ['outGW3']*len(outGW3)+['outPSO3']*len(outPSO3)+['outDE3']*len(outDE3)
tukey_results_G15 = pairwise_tukeyhsd(v, labels, 0.05)
print('Teste Tukey para G15:', tukey_results_G15)













