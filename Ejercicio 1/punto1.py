#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 12:08:00 2018

@author: laiunce
"""

# ---------- > WORKINGDIRECTORY
import os
working_directory = '/Users/laiunce/Documents/evalua/Ejercicio 1'
os.chdir(working_directory)
# < ---------- WORKINGDIRECTORY


from pandas.io.json import json_normalize
import requests
import pandas as pd
import numpy as np
import os



# la api no tiene filtro de fechas por lo que el filtrado se realiza una vez descargada la informacion desde la api y filtrando con dataini y datafin


#parametros filtrado
moneda='BTC'
mercado = 'CNY'
dateini = '2018-01-01'
datefin = '2018-03-25'



path = "https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&symbol={}&market={}&apikey=demo#jso".format(moneda,mercado)
r = requests.get(path) 
json = r.json()


data_por_tiempo = json['Time Series (Digital Currency Daily)']


dataset = pd.DataFrame() 
for i in data_por_tiempo:
    try:
        #formato año mes dia se eliminan guiones para tener un incremental independiente de la fecha
        norm=json_normalize(data_por_tiempo[i])
        norm['fecha'] = i.replace('-','')
        dataset = dataset.append(norm)
    except:
        pass
    
#filtrado


dataset_filtrofech = dataset[(dataset['fecha'] >= dateini.replace('-','')) & (dataset['fecha'] <= datefin.replace('-',''))]
dataset_filtrofech.to_csv(working_directory+'/salida.csv',index=False)








