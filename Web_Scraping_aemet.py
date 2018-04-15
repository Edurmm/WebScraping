import json
import requests
#import http.client

url = "https://opendata.aemet.es/opendata/api/red/especial/radiacion/"

querystring = {"api_key":"eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJlZHVybW1AZ21haWwuY29tIiwianRpIjoiYmU0ZWYxMTItNjNjYi00M2UxLWJkZDYtMDdjOWE2MTYxNDU0IiwiaXNzIjoiQUVNRVQiLCJpYXQiOjE1MjM3MjU4NjEsInVzZXJJZCI6ImJlNGVmMTEyLTYzY2ItNDNlMS1iZGQ2LTA3YzlhNjE2MTQ1NCIsInJvbGUiOiIifQ.WG8SOoiHVS5si-O9r-_MZFKKqGqEY1rhVK6sqbjZSR8"}

headers = {
    'cache-control': "no-cache"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
type(response)

response.content.decode("utf-8")
data = response.json()
type (data)
print (data)


datos = requests.get(data["datos"],headers=headers )
print(type(datos))
#datos.content.decode("utf-8")
#data1 = datos.json()

#print(type(data))
#print(data[1]) 
