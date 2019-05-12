
# coding: utf-8
# Norma Carolina Javier Gonzalez.
# Consultas a una api usando RestFul.
# Entorno de desarrollo: jupyter notebook

#Importamos librerias
import requests
import json
from IPython.display import SVG, display

def peticionApi(pais):
    # Creamos la petición HTTP con GET:
    URL = "https://restcountries.eu/rest/v2/"#Guardamos la url
    PARAMS = "name/"+ pais #Guardamos los parametros
    resp = requests.get(URL + PARAMS)#Solicitamos los datos

    if (resp.status_code == 200): #Verificamos que tenga datos
        txt = resp.text #Lo guardamos en una variable

        if (txt[0] == "["): #Si el primer caracter es [ entonces eliminamos el primero y el ultimo
            txt = txt[ 1:len(txt) - 1]

        objDicc = json.loads(txt) #Cargamos el archivo en formato json

        return objDicc;
    else:
        return "nada"

#Capturamos los datos
pais = input("Introduce el nombre del país que requiera buscar: ")
print ("La cadena que ingreso es: ",pais, "\n")#Imprimimos el dato ingresado

obj = peticionApi(pais); #Mandamos a llamar a la función para conectarnos a la api
#Esta función nos retorna un diccionario
#print(type(obj))

if (obj != "nada"):
    urlImg = obj["flag"] #Extraemos la imagen

    #Imprimimos los datos
    print("Nombre del Pais: ", obj["name"], "\n",
          "Capital: ", obj["capital"], "\n",
          "Habitantes: ", obj["population"], "\n",
          "Bandera (url): ", urlImg, "\n"
         )

    display(SVG(url=urlImg)) #Imprimimos la imagen  
else:
    print("Ese pais no existe!")

