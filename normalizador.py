from ngram import NGram
from negocio import *
from modelo import *
from collections import Counter
from logging import *


CD = "COMUNA DESCONOCIDA"
RD = 'REGION DESCONOCIDA'
DD = 'DIRECCIÓN DESCONOCIDA'
RANGO_REGION = 0.8
RANGO_COMUNA = 0.8
RANGO_COMUNA_REGION = 0.9
RANGO_CALLE = 0.8

#USO ESTA
def obtener_region(list_direccion):
    lis_dir = normalizar_altuar(" ".join(list_direccion))[-1].split()
    if not list_direccion:
        return RD
    else:
        mach_region = []
        str_region = []
        lista_ASC_mach = []
        region_direccion = []
        datos_CSV_regiones = CSV_selecAllRegiones()
        for x in formatear_direccion(" ".join(datos_CSV_regiones)):
            for l in x.split():
                for d in lis_dir:
                    if NGram.compare(d,l) >= RANGO_REGION:
                        mach_region.append(l)
        
        mach_region = [x for x in mach_region if x != None]
        for c in range(len(datos_CSV_regiones)):
            str_region.append((c, datos_CSV_regiones[c]))

        n = NGram(str_region, key=lambda x: x[1])
        lista_ASC_mach = n.search(" ".join(set(mach_region)))

        if not lista_ASC_mach:
            region_direccion.append(RD)
            return "".join(region_direccion[:1])
        else:
            for x in lista_ASC_mach:
                reg,prob = x
                num, nom = reg
                region_direccion.append(nom)

        return "".join(region_direccion[:1])


#SOLO SI NO SE TIENE REGION
def obtener_comuna(list_direccion):
    
    if not list_direccion:
        return CD
    else:
        lis_dir = normalizar_altuar(" ".join(list_direccion))[-1].split()
        mach_comuna = []
        str_comuna = []
        lista_ASC_mach = []
        comuna_direccion = []
        datos_CSV_comunas = CSV_selecAllComunas()
        for x in formatear_direccion(" ".join(datos_CSV_comunas)):
            for l in x.split():
                for d in lis_dir:
                    if NGram.compare(d,l) >= RANGO_COMUNA:
                        mach_comuna.append(l)
        
        mach_comuna = [x for x in mach_comuna if x != None]
        for c in range(len(datos_CSV_comunas)):
            str_comuna.append((c, datos_CSV_comunas[c]))
        

        n = NGram(str_comuna, key=lambda x: x[1])
        lista_ASC_mach = n.search(" ".join(set(mach_comuna)))

        if not lista_ASC_mach:
            comuna_direccion.append(CD)
            return comuna_direccion
        else:
            for x in lista_ASC_mach:
                reg,prob = x
                num, nom = reg
                comuna_direccion.append(nom)

        return comuna_direccion[:4]



#OBTENER COMUNA DIOS NO BORRAR MAS COMPLETO SIN LLAMAR A DIRECCIONES CON CALLE- REGION
def obtener_comuna_final(region,list_direccion):
    list_direccion = normalizar_altuar(" ".join(list_direccion))[-1].split()
    comunas_de_region = []
    list_comunas = []
    lista_ASC_mach = []
    mach_comuna=[]
    comuna_deRegion=[]

    if "".join(region) == RD:
        # print("1")
        comuna_generl =  obtener_comuna(list_direccion)
        if not comuna_generl:
            # print("1-1")
            return CD
        elif comuna_generl == CD:
            # print("1-2")
            return CD #SE PUEDRIA SACAR DE LA CALLE PERO AY CASSO DE 3 CALLES LLAMADAS IGUAL EN LA REGION ???? Y SE DEMORA MUCHO CUANDO AY MUCHAS CALLES EN LA REGION
        else:
            # print("1-3")
            return "".join(comuna_generl[:1])#ENTREFO COMUNA, PERO NO TENGO LA REGION POR ENDE SI ES RD pero consegui comuna preguntar en un metodo intermedio call region from x comuna


    elif list_direccion.count(region) == 1 or list_direccion.count("SANTIAGO") == 1 or list_direccion.count("BIO") == 1:#EVITO QUE LA COMUNA SE VEA AFECTADA POR LA REGION, PRIORISO Q ME MUESTRE LA REGION ANTES QUE LA COMUNA
        # print("2")
        comunas_de_region = CSV_selecComunas_Regiones(region)

        for x in comunas_de_region:
            for l in x.split():
                for d in list_direccion:
                    if NGram.compare(d,l) >= RANGO_COMUNA_REGION:
                        mach_comuna.append(x) 

        mach_comuna = [x for x in mach_comuna if x != None]
         # ME DA MACH UNUA COMUNA CON EL NOMBRE IGUAL A LA REGION, Y LO QE SE QUIERE ES DEJAR COMO REGION ESA SIMITUD YA QUE COINCIDIO 1 VEZ NOMAS
        o = NGram(mach_comuna[:3])
        o.remove('SANTIAGO')
        o.remove('ALTO BIOBIO')
        o.remove(region)

        # ORDENA LA LISTA QUE ENTREGO EL MACH MAS ALTO
        for c in range(len(comunas_de_region)):
            list_comunas.append((c, str(comunas_de_region[c])))  
            n = NGram(list_comunas, key=lambda x: x[1]) 

        # ORDENA LA LISTA QUE ENTREGO EL MACH MAS ALTO
        for f in list_direccion:
            lista_ASC_mach = n.search(" ".join(set(o)))
    
        #ORDENA LA LISTA QUE ENTREGO EL MACH MAS ALTO
        for x in lista_ASC_mach:
            comu,prob = x
            num, nom = comu
            comuna_deRegion.append(nom)

        if not comuna_deRegion:
            #PODRIAMOS SACAR COMUNA DE LA CALLE Y LA REGION
            # print("2-1")
            return CD
        else:
            # print("2-2")
            return  "".join(comuna_deRegion[:1])
       
    else: #SI AY COMUNA Y REGION , ESTE SERIE EL ESESANRIO IDEAL
        comunas_de_region = []
        comunas_de_region = CSV_selecComunas_Regiones(region)

        for x in comunas_de_region:
            for l in x.split():
                for d in list_direccion:
                    if NGram.compare(d,l) >= RANGO_COMUNA_REGION:
                        mach_comuna.append(x) 

        mach_comuna = [x for x in mach_comuna if x != None]
        # print("3")
       # ORDENA LA LISTA QUE ENTREGO EL MACH MAS ALTO
        for c in range(len(comunas_de_region)):
            list_comunas.append((c, str(comunas_de_region[c])))  

            n = NGram(list_comunas, key=lambda x: x[1]) 

        
        # ORDENA LA LISTA QUE ENTREGO EL MACH MAS ALTO
        for f in list_direccion:
            lista_ASC_mach = n.search(" ".join(set(mach_comuna)))
        
        #ORDENA LA LISTA QUE ENTREGO EL MACH MAS ALTO
        for x in lista_ASC_mach:
            comu,prob = x
            num, nom = comu
            comuna_deRegion.append(nom)

        if not comuna_deRegion:
            #PODRIAMOS SACAR COMUNA DE LA CALLE Y LA REGION
            # print("3-1")
            return CD
        else:
            # print("3-2")
            return  "".join(comuna_deRegion[:1])
       
    
        
def obtener_calle_final(region, comuna, list_direccion):
    calles_comuna =[]
    calle_comReg = normalizar_altuar(" ".join(list_direccion))
    direccion_altura = " ".join(calle_comReg[:1]).replace(" ","")
    mach_calle = []
    # print("REGION_CALLE     :" + str(region))
    # print("REGION_COMUNA    :" + str(comuna))
    # print("REGION_DIRECCION   :" + str(direccion_altura))
    if "".join(comuna) == CD:
        calles_region= []
        #puede que tenga region y calle
        calles_region =  CSV_selecCalleXRegion(region)
        for x in calles_region:
            if x != x:
                pass
            else:                  
                if NGram.compare(str(" ".join(formatear_direccion(x)).replace(" ","")),direccion_altura) >= RANGO_CALLE:
                    mach_calle.append(x) 

        mach_calle = [x for x in mach_calle if x != None] 

        if not mach_calle:
            resultado = [DD ,CD, region]
            # print("1")
            return resultado
        else:
            # print("1-2")
            comunaXCalle = CSV_selecComunaXCalle(" ".join(set(mach_calle[:1])), "".join(region))
            resultado = [" ".join(set(mach_calle[:1])) ,comunaXCalle, "".join(region)]

            return resultado
    elif "".join(region) == RD:

        if "".join(comuna) == CD:
            resultado = [DD ,CD, RD]
            # print("2")

            return resultado
        else:
            # print("3")
            calles_comuna =  CSV_selecCalleXComuna(comuna)
            region = CSV_selecRegion_Comuna(comuna)

            for x in calles_comuna:
                if x != x:
                    pass
                else:                  
                    if NGram.compare(str(" ".join(formatear_direccion(x)).replace(" ","")),direccion_altura) >= RANGO_CALLE:
                        mach_calle.append(x) 
      

            mach_calle = [x for x in mach_calle if x != None]           

            if not mach_calle:
                # print("4")
                resultado = [DD ,comuna, " ".join(set(region))]
                return resultado
            else: 
                # print("5")
                resultado = [" ".join(set(mach_calle[:1])) ,comuna, "".join(set(region))]
                return resultado

    else:        
        calles_comuna =  CSV_selecCalleXComuna(comuna)
        for x in calles_comuna:
            if x != x:
                pass
            else:     
                if NGram.compare(str("".join(formatear_direccion(x)).replace(" ","")),direccion_altura) >= RANGO_CALLE:
                    mach_calle.append(x)

        mach_calle = [x for x in mach_calle if x != None]           

        if not mach_calle:
            # print("6")
            resultado = [DD ,comuna, region]
            return resultado
        else: 
            # print("7")
            resultado = [" ".join(set(mach_calle[:1])) ,comuna, region]
            return resultado

        
