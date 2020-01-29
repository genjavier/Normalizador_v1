import re
from unicodedata import normalize
import pandas
from numeros import * 


def formatear_direccion(str_direccion):
    str_direccion = str(str_direccion)
    if not str_direccion:
        return "INGRESA UNA DIRECCIÓN"
    else:
        s = str_direccion.lower()
        s = re.sub(r"([^\u0300-\u036f]|(?!\u0303(?![\u0300-\u036f])))[\u0300-\u036f]+", r"\1", normalize( "NFD", s), 0, re.I  )
        s = normalize( 'NFC', s)
        s = re.sub(r"[-()\"#/@;:<>{}`+=~|.!?,$&°'%]", "  ", s)
        a = s.replace("lib ", "libertador ")
        b = a.replace("gral ", "general ")
        c = b.replace("gen ", "general ")
        d = c.replace("gr ","general ")
        e = d.replace("biobio","bio ")
        f = e.replace("bio bio ","bio ")
        g = f.replace("sn", "0000")
        palabras = g.split()
        PALABRAS_COMUNES = ['LA',"Y","LO",'LOS',"LAS",'DE','EL','DEL',"O","EN","SAN","PUERTO","RIO","PJE", "AV","AVDA","PSJE"]
        reformado = ['' if palabra.upper() in PALABRAS_COMUNES else palabra.upper() for palabra in palabras]
    
        for x in range(len(reformado)):
            if len(reformado) <= 1 and reformado[x].isnumeric():
                return "SE REQUIEREN MAS DATOS"
            else:
                if reformado[0].isnumeric():
                    reformado[0] = numero_a_letras(int(reformado[0]))
            
        return reformado


def normalizar_altuar(str_direccion):
    dir_split = str_direccion.split()
    nueva_lista = []
    for x in dir_split:
        if  x.isnumeric():
            return str_direccion.split(x)
            break
        else:
            nueva_lista.append(x)

    return nueva_lista


