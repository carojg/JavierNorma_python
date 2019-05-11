
# coding: utf-8
# Norma Carolina Javier Gonzalez.
# Consultas a una api usando RestFul.
# Entorno de desarrollo: jupyter notebook

#Importamos librerias
import requests
import json
from IPython.display import SVG, display

#Capturamos los datos
pais = input("Introduce el nombre del país que requiera buscar: ")

print ("La cadena que ingreso es: ",pais, "\n")#Imprimimos el dato ingresado
# Creamos la petición HTTP con GET:
URL = "https://restcountries.eu/rest/v2/"#Guardamos la url
PARAMS = "name/"+ pais #Guardamos los parametros
resp = requests.get(URL + PARAMS)#Solicitamos los datos

if (resp.status_code == 200): #Verificamos que tenga datos
    txt = resp.text #Lo guardamos en una variable

    if (txt[0] == "["): #Si el primer caracter es [ entonces eliminamos el primero y el ultimo
        txt = txt[ 1:len(txt) - 1]
    
    obj = json.loads(txt) #Cargamos el archivo en formato json
    
    urlImg = obj["flag"] #Extraemos la imagen

    #Imprimimos los datos
    print("Nombre del Pais: ", obj["name"], "\n",
          "Capital: ", obj["capital"], "\n",
          "Habitantes: ", obj["population"], "\n",
          "Bandera (url): ", urlImg, "\n"
         )
    
    display(SVG(url=urlImg)) #Imprimimos la imagen    

