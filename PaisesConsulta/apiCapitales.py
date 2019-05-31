
# coding: utf-8

# Norma Carolina Javier Gonzalez.
# Consultas a una api usando RestFul.
# Entorno de desarrollo: jupyter notebook

#Importamos librerias
import requests
import json
from IPython.display import SVG, display
import pymysql #Esta libreria permite la conexión a mysql

class Api:
    def __init__(self, pais):
        self.pais = pais

    def peticionApi(self):
        # Creamos la petición HTTP con GET:
        URL = "https://restcountries.eu/rest/v2/"#Guardamos la url
        PARAMS = "name/"+ self.pais #Guardamos los parametros
        resp = requests.get(URL + PARAMS)#Solicitamos los datos

        if (resp.status_code == 200): #Verificamos que tenga datos
            txt = resp.text #Lo guardamos en una variable

            if (txt[0] == "["): #Si el primer caracter es [ entonces eliminamos el primero y el ultimo
                txt = txt[ 1:len(txt) - 1]

            objDicc = json.loads(txt) #Cargamos el archivo en formato json

            return objDicc;
        else:
            return None

class Pais:
    def __init__(self, pais):
        api = Api(pais)
        pais = api.peticionApi()
        if (pais != None):
            self.urlImg = pais["flag"] #Extraemos la imagen
            self.name = pais["name"] #Extraemos el nombre
            self.population = pais["population"] #Extraemos los habitantes
            self.capital = pais["capital"] #Extraemos la capital
            self.verific = True
        else:
            self.verific = False

    def insertar(self):
        #Creamos nuestra conexion
        db = pymysql.connect("localhost","root","","paises")
        # preparamos el objeto cursor usando el metodo cursor()
        cursor = db.cursor()

        # Preparamos la sentencia SQL para insertar en la BD.
        sql = "INSERT INTO paises (nombre, numero_habitantes, url_bandera, capital) VALUES (%s, %s, %s, %s)"
        val = (self.name, self.population, self.urlImg, self.capital)
        
        cursor.execute(sql, val)#Ejecutamos la consulta

        if (self.verific == True):
            db.commit()
            print(cursor.rowcount, "Fila Insertada.")
            # desconectar del servidor
            db.close()

#Capturamos los datos
myPais = input("Introduce el nombre del país que requiera buscar: ")
print ("La cadena que ingreso es: ",myPais, "\n")#Imprimimos el dato ingresado

mexico = Pais(myPais)#Mandamos a llamar a la clase pais para conectarnos a la api

if (mexico.verific == True):
    #Imprimimos los datos
    print("Nombre del Pais: ", mexico.name, "\n",
          "Capital: ", mexico.capital, "\n",
          "Habitantes: ", mexico.population, "\n",
          "Bandera (url): ", mexico.urlImg, "\n"
         )

    display(SVG(url=mexico.urlImg)) #Imprimimos la imagen  
    
    mexico.insertar(); #LLamamos a la función insertar
else:
    print("Ese pais no existe!")

