import requests
import funciones

"""
Pendientes:
    * Realizar una grafica entre intensidad de la luz y el tiempo (REALIZADO)
    ** Realizar una grafica entre intensidad de corriente y el tiempo
    ** Obtener datos del Equipo y guardarlos en hoja de datos
    * Sacar los promedios del panel solar (REALIZADO)
"""
"""
DESACTIVADA LA SALIDA DE DATOS POR TERMINAL
print('\n\nUBICACION\n Pais=',country_add,'\n Latitud=',coords_add[1],'\n Longitud=',coords_add[0])
print('\n\nCLIMA\n El clima es=',main_add,',',description_add)
print('\n\nTEMPERATURA\n Temperatura=',temp_add,'c','\n Temperatura maxima=',temp_max_add,'c','\n Temperatura minima=',temp_min_add,'c')
print('\n\nPARAMETROS ESPECIFICOS\n Presion=',pressure_add,'hPa','\n Humedad=',humidity_add,'%','\n Visibilidad=',visibility_add,'m','\n Velocidad del viento=',speed_add,'m/s','\n Porcentaje de nubosidad=',clouds_add,'%')
print('\n\nPARAMETROS DE TIEMPO\n Fecha=',date_add,'\n Salida del sol=',sunrise_add,'\n Puesta del sol=',sunset_add)
print('\n')
"""

def weather_export():
    api_address='http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q=36780,MX'
    # CP = input('Codigo Postal seguido de una coma y la abreviatura del pais en mayusculas: ')
    # url = api_address + CP
    json_data = requests.get(api_address).json()

    # Ubicacion
    coords_add = [json_data["coord"]["lon"],json_data["coord"]["lat"]]
    country_add = json_data["sys"]["country"]

    # Clima descrito sencillo
    main_add = json_data["weather"][0]['main']
    description_add = json_data["weather"][0]["description"]

    # Temperatura
    temp_add = funciones.Round2Three(funciones.Kel2Cel(json_data["main"]["temp"]))
    temp_max_add = funciones.Round2Three(funciones.Kel2Cel(json_data["main"]["temp_max"]))
    temp_min_add = funciones.Round2Three(funciones.Kel2Cel(json_data["main"]["temp_min"]))

    # Parametros especificos
    pressure_add = json_data["main"]["pressure"]
    humidity_add = json_data["main"]["humidity"]
    visibility_add = json_data["visibility"]
    speed_add = json_data["wind"]["speed"]
    clouds_add = json_data["clouds"]["all"]

    # Tiempo
    date_add = funciones.Timestamp2Date(json_data["dt"])
    sunrise_add = funciones.Timestamp2Hours(json_data["sys"]["sunrise"])
    sunset_add = funciones.Timestamp2Hours(json_data["sys"]["sunset"])
    
    weather = {
        "Longitud":coords_add[0],
        "Latitud":coords_add[1],
        "Pais":country_add,
        "Estado":main_add,
        "Descripcion":description_add,
        "Temperatura":temp_add,
        "Temperatura Maxima":temp_max_add,
        "Temperatura Minima":temp_min_add,
        "Presion":pressure_add,
        "Humedad":humidity_add,
        "Visibilidad":visibility_add,
        "Velocidad":speed_add,
        "Nubosidad":clouds_add,
        "Fecha":date_add,
        "Nadir":sunrise_add,
        "Cenit":sunset_add
    }
    
    return weather