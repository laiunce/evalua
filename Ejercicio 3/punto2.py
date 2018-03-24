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

def asigna_tipo_emp(val_2001,val_2006):
    if val_2001== 0 and val_2006 ==1:
        return 'Starter'
    if val_2001== 1 and val_2006 ==0:
        return 'Stopper'
    if val_2001== 1 and val_2006 ==1:
        return 'Cont. Exporter'   
    if val_2001== 0 and val_2006 ==0:
        return 'Cont. Non-Exporter'    

def expo0102(val_2001,val_2002):
    try:
        if val_2001== 0 and val_2002 ==1:
            return '1'   
        else:
            return '0'
    else:
        return '0'

datos_ine_ = pd.read_excel('datos_ine.xlsx', sheet_name= 'Datos')


#PUNTO 2


subset = datos_ine_[['expval','nui','year']]

tabla_pivote = subset.pivot_table(index='nui', columns='year', aggfunc=len, fill_value=0)
tabla_pivote.columns = ['2001','2002','2003','20014','2005','2006']

tabla_pivote['tipo_empresa']= tabla_pivote.apply(lambda row: asigna_tipo_emp(row['2001'], row['2006']), axis=1)

#asigna nombre empresa
tabla_pivote['nom_emp'] = tabla_pivote.index.values

#asigna clasificacion por empresa
merged_data =pd.merge(datos_ine_, tabla_pivote[['tipo_empresa','nom_emp']], left_on='nui', right_on='nom_emp')


#crea tablas por tipo de empresa anualmente

#por exportaciones
subset_ventas = merged_data[['tipo_empresa','fabval','year']]
tabla_ventas_promedio = subset_ventas.groupby(['tipo_empresa', 'year'], as_index=False).mean()
tabla_ventas_mediana = subset_ventas.groupby(['tipo_empresa', 'year'], as_index=False).median()


#por exportaciones
subset_emp = merged_data[['tipo_empresa','emptot','year']]
tabla_empleo_promedio = subset_emp.groupby(['tipo_empresa', 'year'], as_index=False).mean()
tabla_empleo_mediana = subset_emp.groupby(['tipo_empresa', 'year'], as_index=False).median()

