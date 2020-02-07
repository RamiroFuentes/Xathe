# Funciones de tiempo
def horaActual():
    from datetime import datetime

    tiempo = str(datetime.now().time())
    horas =  float(tiempo[0:2])
    minutos =  float(tiempo[3:5])
    segundos =  float(tiempo[6:])
    Thoras = horas + minutos/60 + segundos/3600
    return Thoras

def Timestamp2Hours(Timestamp):
    import time
    hours = time.ctime(Timestamp)
    hours = hours[11:19]
    return hours

def Timestamp2Date(Timestamp):
    import time
    date = time.ctime(Timestamp)
    date = date[0:10]
    return date

# Funciones de Temperatura
def Kel2Cel(kelvin):
    celsius = kelvin - 273.15;
    return celsius


# Funciones numericas
def Round2Three(number):
    Round = round(number,3)
    return Round

# Traductor de datos en python 
