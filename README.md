SolaRadiationAemetscraper
Español

Extrae los datos recopilados por Aemet de radiación solar 

Para ejecutar el script es necesario instalar la siguientes bibliotecas:

csv
json
requests
pandas

El script se debe ejecutar de la siguiente manera:

python foodPriceScraper.py --startDate 01/11/2017 --endDate 04/11/2017

Donde startDate es la fecha de inicio y endDate es la fecha de fin del intervalo de tiempo que se deseea extraer. Los registros se almacenan en un archivo de tipo CSV.

Actualmente Extrae datos de raciación Global, directa, difusa, UV e Infraroja de 35 estaciones de España






Recursos

    Masip, D. (2010). El lenguaje Python. Editorial UOC
    Lawson, R. (2015). Web Scraping with Python. Packt Publishing Ltd. Chapter 2. Scraping the Data.
    Simon Munzert, Christian Rubba, Peter Meißner, Dominic Nyhuis. (2015). Automated Data Collection with R: A Practical Guide to Web Scraping and Text Mining. John Wiley & Sons.
