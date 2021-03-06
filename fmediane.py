# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 10:34:09 2018

@author: jjacq
"""

from recomposition_spectrale import posttrait
import numpy as np
import pandas as pd

# In[1] Chargement des input

# instruction with qui permet de fermer le fichier si erreur ds le block 
with open("Input.txt","r") as fich:
    datain = fich.readlines()

i = 0
num = np.zeros([np.size(datain),1])
for st in datain:
    st1 = np.int(st.split("=")[1].split("\n")[0])
    num[i] = st1
    i += 1
    
    
fref = num[0]# frequence de référence pour le calcul des fréquences limites
fe = num[1]# frequence d'échantillonnage
fmin_bf = num[2]# frequence limite bf
octbf = num[3]# valeur du filtre nième d'octave

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
                    
## Sauvegarde
writer = pd.ExcelWriter('frequence.xlsx')
f.to_excel(writer,'Sheet1')
                    
                    








