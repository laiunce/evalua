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




plt.plot(v_open, color='g')
plt.plot(v_close, color='b')
plt.plot(v_avg, color='r')
plt.xlabel('verde: apertura, azul: cierre, rojo: promedio')
plt.ylabel('dia')
plt.title('cotizaciones y promedio')
plt.show()




