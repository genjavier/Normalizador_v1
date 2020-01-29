from normalizador import *
from numeros import *
import os




dires = [
    "JOSE MANUEL BALMACEDA 2125 Metropolitana"
    ,"VILLA LAS ASUCENAS 2 Metropolitana de Sa"
    ,"EL FILODENDRO1 1774 Metropolitana de San"
    ,"ALEJANDRO GALAZ 4228 VILLA MACU Metropol"
    ,"BLANCO ENCALADA 1335 PLAZA MAYO Metropol"
    ,"PJE ANDALUCIA 8456 Metropolitana de Sant"
    ,"FREIRE 1070 0 Lib. Gral. Bernardo O'Higg"
    ,"MARTINEZ DE ROZAS 3866 Metropolitana de "
    ,"CALLE LA RUDA NR 18 CERRO MAR 0 Valparaí"
    ,"CARLOS IRIBARREN CONDELL 101 Lib. Gral. "
    ,"AVDA EL BOSQUE SUR 90 Metropolitana de S"
]

def prueba_final():
    # direcciones =  dires
    # direcciones = BD_sel_direcciones()
    directorio = os.getcwd()
    direcciones = CSV_selecAll()
    d  = []
    co = []
    r  = []
    ca = []
    con = []
    cont = 0
    for x in direcciones:
        formateo = formatear_direccion(x)
        region = obtener_region(formateo)
        comunas_Region = obtener_comuna_final(region,formateo)
        callesita = obtener_calle_final(region,comunas_Region,formateo)
        cont += 1
        con.append(cont)
        d.append(x)
        co.append(callesita[1])
        r.append(callesita[2])
        ca.append(callesita[0])

    dict = {"num": con ,'DIRECCION': d, "CALLE": ca,'COMUNA': co, 'REGION': r}  
    df = pandas.DataFrame(dict) 
    df.to_csv(r''+str(directorio) + '\\Final_0_4.csv',sep ="|", index=False) 
    

prueba_final()




# MARCOS PEREZ 146  PUENTE ALTO  Metropolitana de Santiago  //  SIN REGISTRO DE CALLE|PUENTE ALTO|METROPOLITANA DE SANTIAGO
# NORMANDIA 1965  PROVIDENCIA  Metropolitana de Santiago   //   SIN REGISTRO DE CALLE|PROVIDENCIA|METROPOLITANA DE SANTIAGO
# 1872|"""JOSE MANUEL BALMACEDA 2125 Metropolitana""  "|DIRECCIÓN DESCONOCIDA|COMUNA DESCONOCIDA|HACER MACH CON REGION ?????
# 1873|"""VILLA LAS ASUCENAS 2 Metropolitana de Sa""  "|DIRECCIÓN DESCONOCIDA|COMUNA DESCONOCIDA|HACER MACH CON REGION ?????
# 1874|"""EL FILODENDRO1 1774 Metropolitana de San""  "|DIRECCIÓN DESCONOCIDA|COMUNA DESCONOCIDA|HACER MACH CON REGION ?????
# 1875|"""ALEJANDRO GALAZ 4228 VILLA MACU Metropol"" "|DIRECCIÓN DESCONOCIDA|COMUNA DESCONOCIDA|HACER MACH CON REGION ?????
# 1876|"""BLANCO ENCALADA 1335 PLAZA MAYO Metropol"" "|DIRECCIÓN DESCONOCIDA|COMUNA DESCONOCIDA|HACER MACH CON REGION ?????
# 1877|"""PJE ANDALUCIA 8456 Metropolitana de Sant""  "|DIRECCIÓN DESCONOCIDA|COMUNA DESCONOCIDA|HACER MACH CON REGION ?????
# 1878|"""FREIRE 1070 0 Lib. Gral. Bernardo O'Higg""  "|DIRECCIÓN DESCONOCIDA|COMUNA DESCONOCIDA|HACER MACH CON REGION ?????
# 1879|"""MARTINEZ DE ROZAS 3866 Metropolitana de ""  "|DIRECCIÓN DESCONOCIDA|COMUNA DESCONOCIDA|HACER MACH CON REGION ?????
# 1880|"""CALLE LA RUDA NR 18 CERRO MAR 0 Valparaí""  "|DIRECCIÓN DESCONOCIDA|COMUNA DESCONOCIDA|HACER MACH CON REGION ?????
# 1881|"""CARLOS IRIBARREN CONDELL 101 Lib. Gral. ""  "|DIRECCIÓN DESCONOCIDA|COMUNA DESCONOCIDA|HACER MACH CON REGION ?????
# 1882|"""AVDA EL BOSQUE SUR 90 Metropolitana de S"" 


# x = "DIECIOCHO DE SEPTIEMBRE 1170  CHILLAN  Biobío" error de comuna y region


# x = 'L PENON FERROCARRIL 1380 Coquimbo'   //ojo con esta

# x = "PASAJE SAN JOSE 1520  NUEVA IMPERIAL  La Araucanía"
# x = 'SANTA TERESA,88,Valparaíso'
# x ="AVDA LO ERRAZURIZ,4057,Metropolitana de"
# # x ="PSJE CARDENAL CARO,1465,Metropolitana de"
# x = "|LOS NOGALES,342,Biobío"

# LIBERTADOR GENERAL BERNARDO O HIGGINS,GRANEROS,VEINTIUNO DE MAYO
# LIBERTADOR GENERAL BERNARDO O HIGGINS,RANCAGUA,VEINTIUNO DE MAYO

# x = "21 DEMAYO,555,  Lib. Gral. Bernardo O'Higgi"

# x = 'SANTA CLARA 2765 Metropolitana de Santia' // cuarentamil calles y pasajes qe se llaman igual en una misma region

# x =  "ANTONI VALECH,2188,Metropolitana de Sant"
# x = "PASAJE CAUQUENES,1251,Tarapacá"
# x = "PROFESOR ALCAINO,01469,DPTO14U,Metropoli"

# x ="AVENIDA  JOSE MANUEL BALMACEDA, 60, LA SERENA, Coquimbo"

# x= "UNO NORTE, 1951, TALCA, Maule"

# x = "AVENIDA LIBERTADOR BERNARDO OHIGGINS, 1493, 34100359, ABarrio, Metropolitana de Santiago"
# x = "AVENIDA LIBERTADOR BERNARDO OHIGGINS, 1449,  RANCAGUA, Metropolitana de Santiago"
# x = "AVENIDA DEL MAR, 4000, LA SERENA, Coquimbo"



# x =  'GENERAL LAGOS, 591-A, VICTORIA, Aisén del Gral. Carlos Ibáñez del Campo'

# x = "SEMINARIO, 385, PROVIDENCIA, Metropolitana de Santiago"
# formateo = formatear_direccion(x)
# region = obtener_region(formateo)
# comunas_Region = obtener_comuna_final(region,formateo)
# callesita = obtener_calle_final(region,comunas_Region,formateo)


# print(formateo)
# print(callesita)
# print(comunas_Region)
# print(region)

# print(str(" ".join(formatear_direccion("SEMINARIO")).replace(" ","")))


# print (numero_a_letras(23123))




# ///////////////  EL ROBLE, 770-115, CHILLAN, Ñuble
# //////////////7 SAN MARTIN, SNV.0, LOS LAGOS, Los Ríos
# //////////////  MARIANO LATORRE, 1892, COIHAIQUE, Aisén del Gral. Carlos Ibáñez del Campo