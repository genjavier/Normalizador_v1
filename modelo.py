import re
from conexion.coneccion import *
import pandas



#region OBTENGO DATOS DESDE DESDE BASE DE DATOS MYSQL ---------------------------------------------------------------------------------

def BD_sel_direcciones():
    sql = "select CONCAT(CONCAT(ADDRESS_LINE_1,' '), CONCAT(ADDRESS_LINE_2,' '),CONCAT(ADDRESS_LINE_3,' '),CONCAT(ADDRESS_LINE_4,' ')) as direccion from direcciones limit 500"
    cursor = select_region(sql)
    lis_dir = []
    for x in cursor:
        lis_dir += x
    return lis_dir

#Trae la comuna y region (comuna,region) segun la comuna.
def BD_sel_comReg(region):
    sql= "select nombre_comuna from region_comuna where  nombre_region = '"+str(region)+ "';"
    cursor = select(sql)
    lis_comReg = []
    for x in cursor:
        lis_comReg += x
    return lis_comReg

def BD_sel_region(comuna):
    sql ="select nombre_region from region_comuna where nombre_comuna = '"+str(comuna)+ "';"
    cursor = select(sql)
    lis_region = []
    for x in cursor:
        lis_region += x
    return lis_region

#Selecciona todas las regiones
def BD_sel_regiones():
    sql = "select nombre_region from regiones"
    cursor = select(sql)
    lis_reg = []
    for x in cursor:
        lis_reg += x
    return lis_reg

#SELECIONA TODAS LAS COMUNAS
def BD_sel_comunas():
    sql = "select nombre_comuna from comunas"
    cursor = select(sql)
    lis_reg = []
    for x in cursor:
        lis_reg += x
    
    # print(lis_reg)
    return lis_reg

#endregion


#region OBTENGO DATOS DE ARCHIVO CSV ---------------------------------------------------------------------------------------


def CSV_selecAll():
    ADDRESS_LINE_1 = []
    col_name  = ["ADDRESS_KEY","ADDRESS_ID","ADDRESS_COMMENT","ADDRESS_LINE_1","ADDRESS_LINE_2","ADDRESS_LINE_3","ADDRESS_LINE_4","APARTMENT","BARRIO","BLOCK","POSTAL_STREET_NAME","POSTAL_STREET_NUMBER","POSTAL_TOWN","STREET","STREET_NUMBER"]
    CSV_direcciones_sucuas  = pandas.read_csv('CSV_lectura\direcciones_sucias.csv', sep='|', names=col_name, encoding = 'utf8').head(20)
    for index, row in CSV_direcciones_sucuas.iterrows():
        ADDRESS_LINE_1 += [row['ADDRESS_LINE_1']]
    
    return ADDRESS_LINE_1




def CSV_selecAllRegiones():
    nombre_region = []
    col_name  = ["id_region","nombre_region","partition_date"]
    CSV_regiones  = pandas.read_csv('CSV_lectura\\REGIONES.csv', sep=',', names=col_name,header=1, encoding = 'utf8')
    for index, row in CSV_regiones.iterrows():
        nombre_region.append(row['nombre_region'])
      
    return nombre_region


def CSV_selecAllComunas():
    nombre_comuna = []
    col_name  = ["nombre_comuna","id_comuna"]
    CSV_comunas = pandas.read_csv('CSV_lectura\\COMUNAS.csv', sep=',', names=col_name,header=1, encoding = 'utf8')
    for index, row in CSV_comunas.iterrows():
        nombre_comuna.append(row['nombre_comuna'])
      
    return nombre_comuna


def CSV_selecComunas_Regiones(region):
    comunas_region = []
    col_name  = ["nombre_region","nombre_comuna"]
    CSV_comuna_regiones  = pandas.read_csv('CSV_lectura\\REGION_COMUNA.csv', sep=',', names=col_name, encoding = 'utf8')
    CSV_comuna_regiones.query('nombre_region == "'+str(region)+'"', inplace = True) 
    for x in CSV_comuna_regiones.nombre_comuna:
        comunas_region.append(x)

    return comunas_region

def CSV_selecRegion_Comuna(comuna):
    comunas_region = []
    col_name  = ["nombre_region","nombre_comuna"]
    CSV_comuna_regiones  = pandas.read_csv('CSV_lectura\\REGION_COMUNA.csv', sep=',', names=col_name, encoding = 'utf8')
    CSV_comuna_regiones.query('nombre_comuna == "'+str(comuna)+'"', inplace = True) 
    for x in CSV_comuna_regiones.nombre_region:
        comunas_region.append(x)

    return comunas_region

def CSV_selecCalle(comuna,region):
    nombre_calle = []
    col_name  = ['nombre_region','nombre_comuna','nombre_calle']
    CSV_calle  = pandas.read_csv('CSV_lectura\\region_comuna_calle.csv', sep=',', names=col_name, encoding = 'utf8')
    CSV_calle.query('nombre_region == "'+str(region)+'" and nombre_comuna == "'+str(comuna)+'" ', inplace = True) 
    for x in CSV_calle.nombre_calle:
        nombre_calle.append(x)

    return nombre_calle

def CVS_nomComRegi_equals(region):

    col_name  = ["nombre_region","nombre_comuna"]
    CSV_comuna_regiones  = pandas.read_csv('CSV_lectura\\REGION_COMUNA.csv', sep=',', names=col_name, encoding = 'utf8')
    xd = CSV_comuna_regiones.loc[CSV_comuna_regiones['nombre_comuna'] == str(region)]
    if xd.empty:
        return False
    else:
        return True  


  
def CSV_iguales():
    nombre_calle = []
    col_name  = ['nombre_region','nombre_comuna']
    CSV_calle  = pandas.read_csv('CSV_lectura\\REGION_COMUNA.csv', sep=',', names=col_name, encoding = 'utf8')
    CSV_calle.query('nombre_region == nombre_comuna', inplace = True) 
    for x in CSV_calle.nombre_region:
        nombre_calle.append(x)

    return nombre_calle

def CSV_selecCalleXComuna(comuna):
    nombre_calle = []
    col_name  = ['nombre_region','nombre_comuna','nombre_calle']
    CSV_calle  = pandas.read_csv('CSV_lectura\\region_comuna_calle.csv', sep=',', names=col_name, encoding = 'utf8')
    CSV_calle.query('nombre_comuna == "'+str(comuna)+'" ', inplace = True) 
    for x in CSV_calle.nombre_calle:
        nombre_calle.append(x)

    return nombre_calle

def CSV_selecCalleXRegion(region):
    nombre_calle = []
    col_name  = ['nombre_region','nombre_comuna','nombre_calle']
    CSV_calle  = pandas.read_csv('CSV_lectura\\region_comuna_calle.csv', sep=',', names=col_name, encoding = 'utf8')
    CSV_calle.query('nombre_region == "'+str(region)+'" ', inplace = True) 
    for x in CSV_calle.nombre_calle:
        nombre_calle.append(x)

    return nombre_calle

def CSV_selecComunaXCalle(calle,region):
    nombre_comuna = []
    col_name  = ['nombre_region','nombre_comuna','nombre_calle']
    CSV_calle  = pandas.read_csv('CSV_lectura\\region_comuna_calle.csv', sep=',', names=col_name, encoding = 'utf8')
    CSV_calle.query('nombre_region == "'+str(region)+'" and nombre_calle == "'+str(calle)+'" ', inplace = True) 
    for x in CSV_calle.nombre_comuna:
        nombre_comuna.append(x)

    return nombre_comuna

#endregion