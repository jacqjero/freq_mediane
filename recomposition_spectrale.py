# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 13:41:01 2018

@author: Claire
"""

import numpy as np
import pandas as pd

def posttrait(f1,f2,f3,bd):
    
    t = np.arange(-100,101,1)
    if np.mod(bd,2) == 0:
        fa = f1*2**((2*t+1)/(2*bd))
    else:
        fa = f1*2**(t/bd)
    
    f = fa[(fa>f3) & (fa<f2/2)]
    f_limb = np.array(f)*2**(-0.5*1/bd)
    f_limh = np.array(f)*2**(0.5*1/bd)
    
    f_bande = pd.DataFrame({'Fc':np.array(f),
                               'Flimb':f_limb,'Flimh':f_limh}).sort_values(by='Fc')
    
    return f_bande


def recomp(f,bd,df,signal,nb):
    
    spectre = np.zeros((nb,))
    nbrpts = np.zeros((nb,))
    for ip in range(0,nb):
        test=f.loc[(f['freq']>bd.iloc[ip,1]) & (f['freq']<bd.iloc[ip,2])]
        deltab = (test.iloc[0,0]-df/2-bd.iloc[ip,1])/(df/2)
        deltah = (bd.iloc[ip,2]-(test.iloc[-1,0]+df/2))/(df/2)
        if deltab > 0:
            imoins = deltab*signal[test.index[0]-1]/2    
        elif deltab < 0:
            imoins = deltab*signal[test.index[0]]/2            
        if deltah > 0:
            iplus = deltah*signal[test.index[-1]+1]/2            
        elif deltah < 0:
            iplus = deltah*signal[test.index[-1]]/2
            
        correction = iplus + imoins
        spectre[ip] = correction + np.sum(signal[test.index]) 
        nbrpts[ip] = np.size(test)
        
    return  spectre,nbrpts