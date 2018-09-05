# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 10:34:09 2018

@author: jjacq
"""

from recomposition_spectrale import posttrait


# In[1] Chargement des input

# instruction with qui permet de fermer le fichier si erreur ds le block 
with open("Input.txt","r") as fich:
    datain = fich.readlines()

fref = datain[0]
fe = datain[1]
fmin_bf = datain[2]
octbf = datain[3]

f = posttrait(fref,fe,fmin_bf,octbf)
for x in f.Fc:
    if x < 100:
        print('{0: >#4.3f}'. format(float(x))) 
    elif (x < 1000 and x >= 100):
        print('{0: >#4.2f}'. format(float(x))) 
    elif (x < 10000 and x >= 1000):
        print('{0: >#4.1f}'. format(float(x)))
    else:
        print('{0: >#5f}'. format(float(x))) 
                    
                    
                    








