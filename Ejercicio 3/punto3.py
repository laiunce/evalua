#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 12:08:00 2018

@author: laiunce
"""



import pandas as pd
import os
working_directory = '/Users/laiunce/Documents/evalua/Ejercicio 3/'
os.chdir(working_directory)


def expo0102(val_2001,val_2002):
    try:
        if val_2001== 0 and val_2002 ==1:
            return '1'   
        else:
            return '0'
    except:
        return '0'
    
def estaenlista(valor,lista):
    if valor in lista:
        return 1
    else:
        return 0

#PUNTO 3

subset = datos_ine_[['expval','nui','year']]
tabla_pivote = subset.pivot_table(index='nui', columns='year', aggfunc=len, fill_value=0)
tabla_pivote.columns = ['2001','2002','2003','20014','2005','2006']
tabla_pivote['filtra']= tabla_pivote.apply(lambda row: expo0102(row['2001'], row['2002']), axis=1)

lista_empresas_0102 = tabla_pivote[tabla_pivote['filtra']=='1'].index.values


#filtra empresas que no exportaron en 2001 pero si en 2002



datos_ine_['expo0102']= datos_ine_.apply(lambda row: estaenlista(row['nui'], lista_empresas_0102), axis=1)
filtrado_expor0102 = datos_ine_[datos_ine_['expo0102'] == 1]


#regresion para 2006
from sklearn import datasets, linear_model
regr = linear_model.LinearRegression()

subset = filtrado_expor0102[['nui','year']]
tabla_pivote = subset.pivot_table(index='nui', columns='year', aggfunc=len, fill_value=0)
tabla_pivote.columns = ['2002','2003','20014','2005','2006']

X = tabla_pivote[['2002','2003','20014','2005']]
Y=tabla_pivote[['2006']]
regr.fit(X, Y)

coeficientes = regr.coef_

#viendo los coeficientes vemos la importancia de cada uno, vemos que 2002 obviaente no tiene peso y el que mas te predice la tasa 
#de continuiedad es el ultimo año, si en 2005 sigue siendo exportador, con un 80% lo va a seguir siendo en 2006




