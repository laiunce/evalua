#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 16:59:10 2018

@author: laiunce
"""

def clean(val):
    if(val=='.' or val < 0 or val is None):
        return False
    else:
        return True
 

import pandas as pd
import os
working_directory = '/Users/laiunce/Documents/evalua/Ejercicio 3/'
os.chdir(working_directory)            

datos_ine_ = pd.read_excel('datos_ine.xlsx', sheet_name= 'Datos')




for index, row in datos_ine_.iterrows():
    if(clean(row['fabval']) and clean(row['expval'])):
        if index == 0:
            datos_ine = pd.DataFrame(row)
            datos_ine = datos_ine.transpose()
        else:
            datos_ine = datos_ine.append(row) 
            
            
# Transformar datos_ine en un panel balanceado                                                        
# datos_ine.groupby(['year']).size()  #todos los registros se encuentran entre 2001 y 2006
nui_years = datos_ine.groupby(['nui']).size().reset_index(name='years')
nui_years = nui_years[nui_years.years == 6]

# datos_ine2 = datos_ine.copy()
for index, row in datos_ine.iterrows():
    if row['nui'] in nui_years['nui'].values.tolist():
        if index == 0:
            datos_ine2 = pd.DataFrame(row)
            datos_ine2 = datos_ine2.transpose() 
        else:
            datos_ine2 = datos_ine2.append(row)

datos_ine = datos_ine2  