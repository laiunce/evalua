#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 12:08:00 2018

@author: laiunce
"""

# ---------- > WORKINGDIRECTORY
import os
working_directory = '/Users/laiunce/Documents/evalua'
os.chdir(working_directory)
# < ---------- WORKINGDIRECTORY

from pandas.io.json import json_normalize
import requests
import pandas as pd
import numpy as np
import os
from datetime import datetime, timedelta


#descompone la serie para investigar ruido
from random import randrange
from pandas import Series
from matplotlib import pyplot
from statsmodels.tsa.seasonal import seasonal_decompose


def analizar_serie_outlier(analiza_serie,porcentaje_cota):
    series = [analiza_serie[i] for i in range(1,len(analiza_serie))]
    # graficamos la serie observando tomando de 3 dias cuales son los componentes estacionales, de tendencia y de ruuido
    result = seasonal_decompose(series, model='additive', freq=3)
    result.plot()
    pyplot.show()
    
    #si el nivel de ruido super porcentaje respecto al valor obsoluto del maximo pico entonces es anomalo
    
    
    residuos = result.resid
    
    
    list_sinnan=[]
    for i in residuos[1:len(residuos)-1]:
        list_sinnan.append(i)
    
    
    #obtiene el maximo valor absoluto
    cota  = max(abs(max(list_sinnan)),abs(min(list_sinnan)))

    
    lista_indices = []
    for i in range(0,len(residuos)):
        if abs(residuos[i]) > cota*porcentaje_cota:
            lista_indices.append(i)
            
    for i in  lista_indices:
        print('pos:'+str(i)+', valor: '+str(analiza_serie[i]))

    
    
diasdelay= 30



diafin = datetime.now().strftime('%Y%m%d')
diainicio = (datetime.now() - timedelta(days=diasdelay)).strftime('%Y%m%d')


dataset = pd.read_csv(working_directory+'/salida.csv')


#ultimos 30 dias desde la fecha


df = dataset[(dataset['fecha'] >= int(diainicio)) & (dataset['fecha'] <= int(diafin))]


v_open = df['1b. open (USD)']
v_close = df['4b. close (USD)']
v_avg = df[['1b. open (USD)', '4b. close (USD)']].mean(axis=1)



import matplotlib.pyplot as plt


#plotea

plt.plot(v_open, color='g')
plt.plot(v_close, color='b')
plt.plot(v_avg, color='r')
plt.xlabel('verde: apertura, azul: cierre, rojo: promedio')
plt.ylabel('dia')
plt.title('cotizaciones y promedio')
plt.show()


# PUNTO 3

#LE INGRESA LA COTA para hacer tecnica por descomposicion si el residuo supera un 50% del maximo desvio lo tilda como outlier de la siere

analizar_serie_outlier(v_open,0.5)

analizar_serie_outlier(v_close,0.5)

analizar_serie_outlier(v_open,0.5)
















    

