#importamos las librerías necesarias

import csv
import json
import requests
import pandas as pd

from datetime import datetime
from datetime import timedelta



#la url de la que vamos a obtener la información
url = "https://opendata.aemet.es/opendata/api/red/especial/radiacion/"

#Clave API
querystring = {"api_key":"eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJlZHVybW1AZ21haWwuY29tIiwianRpIjoiYmU0ZWYxMTItNjNjYi00M2UxLWJkZDYtMDdjOWE2MTYxNDU0IiwiaXNzIjoiQUVNRVQiLCJpYXQiOjE1MjM3MjU4NjEsInVzZXJJZCI6ImJlNGVmMTEyLTYzY2ItNDNlMS1iZGQ2LTA3YzlhNjE2MTQ1NCIsInJvbGUiOiIifQ.WG8SOoiHVS5si-O9r-_MZFKKqGqEY1rhVK6sqbjZSR8"}

headers = {
    'cache-control': "no-cache"
    }

#Extraemos el JSON donde estará nuestra URL
response = requests.request("GET", url, headers=headers, params=querystring)

#Obtenemos la URL del dia 
d = json.loads(response.text)
url_final = (d['datos'])



#Extraemos los datos que vienen en forma de texto

response2 = requests.get(url_final)
d2=response2.text
print(type(d2))


#Sustituimos las ; por comas
d3=d2.replace(";",",")


#Obtenemos los indices básicos
file_list = d3.split('\n')
print (file_list[2])
Index=file_list[2].split(",")
#Extraemos la fecha
Fecha=file_list[1].split(",")


#Arreglamos nuestros indicies para la creación del dataset
y=0
z=0
Tipos=["(GL)","(DF)","(DT)","(UVB)","(IR)"]
for x in Index:
    z=z+1
    if x=="Tipo":
        y=y+1
        Index[z-1]=str(x)+str(Tipos[y-1])
    if (y!=0):
        Index[z-1]=str(x)+str(Tipos[y-1])

#Añadimos el indice fecha
Index.append("fecha")        


#Determinamos el tamaño de la matriz de datos
w=len(Index)
h=len(file_list)



#creamos la matriz de datos


for x in range(h):
    file_list[x]=str(file_list[x])+(",")+str(Fecha[0])
    Matrix[x]=file_list[x].split(',')
    


#función de transposición
def transpuesta(matriz):
    rows = len(matriz)
    cols = len(matriz[0])
    return [[matriz[j][i] for j in range(rows)] for i in range(cols)]

#Eliminamos las filas vacías de nombre y fecha y la de índices 
datos4=Matrix[3:][0:-1]

#Transponemos
matrixt=transpuesta(datos4)



datos5=(matrixt[:][:])

#Creamos el diccionario

dic={}

y=0
for x in Index:
    dic[x]=(datos5[y][:])
    y=y+1
    

print (len (dic))


#Creamos el dataset

dataset=pd.DataFrame(dic)


