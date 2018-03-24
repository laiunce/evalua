

####
####
#se asume tabla TPU ya creada como se muestra en el ejemplo
####
####

####
####
#### 1- DEVICE_ID distintos
####
####

select count (distinct DEVICE_ID)
from
TPU

####
####
#### 2-promedio gastado de los usuarios en TPU
####
####

IF OBJECT_ID('tempdb..#tmp_purch') IS NOT NULL DROP TABLE #tmp_purch;
select
DEVICE_ID, sum(EVENT_VALUE) purch
into #tmp_purch
from
TPU
where EVENT_ID = 2
group by DEVICE_ID

select AVG(purch)
from
#tmp_purch

####
####
#### 3-promedio tiempo entre compras
####
####

IF OBJECT_ID('tempdb..#tmp_tiempo') IS NOT NULL DROP TABLE #tmp_tiempo;
select
DEVICE_ID, 
#diferencia entre fecha actual y fecha con lag 1
MySQL DATEDIFF( EVENT_DATE, lag(EVENT_DATE,1) over (order by EVENT_DATE) ) dias_entre_compra
into #tmp_tiempo
from
TPU
where EVENT_ID = 2
order by DEVICE_ID, EVENT_DATE desc

select 
DEVICE_ID,
avg(dias_entre_compra)
from
#tmp_tiempo
group by DEVICE_ID

