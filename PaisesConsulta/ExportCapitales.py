import pymysql #Esta libreria permite la conexión a mysql
import csv #Nos servirá para leer archivos csv
import xlsxwriter #Nos servirá para leer archivos excel

class ExportExcel: #Esta clase nos servira para exportar a un archivo excel
    def __init__(self, allPaises): #Definimos nuestro constructor
        self.allPaises = allPaises #Guardamos los datos en nuestra lista de diccionarios

    def exportarExcel(self): #Funcion que exporta a excel
        workbook = xlsxwriter.Workbook('paises.xlsx')#Creamos nuestro archivo
        worksheet = workbook.add_worksheet()

        colNum = 0#Nos sirve para llevar el control de las columnas
        for key in allPaises[0]:#Obtenemos los nombres de los campos de la tabla
            worksheet.write(0, colNum, key) # fila, columna, dato
            colNum = colNum + 1#Aumentamos columna

        rowNum = 1 #Filas en 1 puesto que hay un registro
        colNum = 0 #Se reinicia columnas

        # Guardamos los datos
        for pais in allPaises:#Recorremos nuestra lista
            for key in pais.keys():#Recorremos el diccionario dentro de la lista
                worksheet.write(rowNum, colNum, pais[key]) # fila, columna, valor
                colNum = colNum + 1 #Aumentamos columna
            rowNum = rowNum + 1#Aumentamos filas
            colNum = 0 #Restauramos columnas a 0

        workbook.close() #Cerramos nuestro libro

class ExportCsv: #Esta clase nos permite exportar archivos con extension csv
    def __init__(self, allPaises):#Creamos nuestro constructor
        self.allPaises = allPaises # Asignamos nuestra lista de diccionarios

    def exportarCsv(self): #Funcion que exporta archivos csv
        keys = self.allPaises[0].keys() #Obtenemos las claves del diccionario
        with open('paises.csv', mode='w') as csv_file: #Abrimos el archivo y le damos permiso de escritura
            writer = csv.DictWriter(csv_file, fieldnames=keys)#LLenamos el encabezado

            writer.writeheader()
            for pais in allPaises:#Recorremos nuestra lista de diccionarios
                writer.writerow(pais)
        
#Creamos nuestra conexion
db = pymysql.connect("localhost","root","","paises")
# preparamos el objeto cursor usando el metodo cursor()
cursor = db.cursor(pymysql.cursors.DictCursor)

# Ejecutamos nuestra consulta
cursor.execute("SELECT * FROM paises")
allPaises = cursor.fetchall()

excel = ExportExcel(allPaises)#Llamamos a la clase ExportExcel
excel.exportarExcel() #Llamamos a la función para exportar a excel

miCsv = ExportCsv(allPaises)#Llamamos a nuestra clase
miCsv.exportarCsv()#Llamamos a la función para exportar archivos en formato csv