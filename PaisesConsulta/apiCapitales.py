
# coding: utf-8

# Norma Carolina Javier Gonzalez.
# Consultas a una api usando RestFul.
# Entorno de desarrollo: jupyter notebook

#Importamos librerias
import requests
import json
from IPython.display import SVG, display
import pymysql #Esta libreria permite la conexión a mysql

def conexion():
    # creamo la conexion
    db = pymysql.connect("localhost","root","","paises")
    return db

def insertar(name, population, urlImg, capital):
    db = conexion()
    
    # preparamos el objeto cursor usando el metodo cursor()
    cursor = db.cursor()

    # Preparamos la sentencia SQL para insertar en la BD.
    sql = "INSERT INTO paises (nombre, numero_habitantes, url_bandera, capital) VALUES (%s, %s, %s, %s)"
    val = (name, population, urlImg, capital)
    
    cursor.execute(sql, val)#Ejecutamos la consulta

    db.commit()

    print(cursor.rowcount, "Fila Insertada.")
    # desconectar del servidor
    db.close()

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
        return None

#Capturamos los datos
pais = input("Introduce el nombre del país que requiera buscar: ")
print ("La cadena que ingreso es: ",pais, "\n")#Imprimimos el dato ingresado

obj = peticionApi(pais); #Mandamos a llamar a la función para conectarnos a la api

if (obj != None):
    urlImg = obj["flag"] #Extraemos la imagen
    name = obj["name"] #Extraemos el nombre
    population = obj["population"] #Extraemos los habitantes
    capital = obj["capital"] #Extraemos la capital
    
    #Imprimimos los datos
    print("Nombre del Pais: ", name, "\n",
          "Capital: ", capital, "\n",
          "Habitantes: ", population, "\n",
          "Bandera (url): ", urlImg, "\n"
         )

    display(SVG(url=urlImg)) #Imprimimos la imagen  
    
    insertar(name, population, urlImg, capital); #LLamamos a la función insertar
else:
    print("Ese pais no existe!")

