import requests
from bs4 import BeautifulSoup
import pandas as pd


#Declaracion del array que se creara
cedula = []
nombre = []
estado = []
municipio = [] 
parroquia = []
centro = []
direccion = []


print('Ingrese la nacionalidad (V=Venezolano, E=Extranjero): ')
nacionalidad = input()
print('Ingrese la cedula: ')
idx = input()

#Llamado de la pagina con los parametros solicitados
URL = f"http://www.cne.gob.ve/web/registro_electoral/ce.php?nacionalidad={nacionalidad}&cedula={idx}"
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

checking = len(list(soup.find('table'))[5].find('table').table.find_all('tr'))

if checking == 7:

    cedula.append(list(soup.find('table'))[5].find('table').table.find_all('tr')[0].find_all('td')[1].text)

    nombre.append(list(soup.find('table'))[5].find('table').table.find_all('tr')[1].find_all('td')[1].text)

    estado.append(list(soup.find('table'))[5].find('table').table.find_all('tr')[2].find_all('td')[1].text)

    municipio.append(list(soup.find('table'))[5].find('table').table.find_all('tr')[3].find_all('td')[1].text)

    parroquia.append(list(soup.find('table'))[5].find('table').table.find_all('tr')[4].find_all('td')[1].text)

    centro.append(list(soup.find('table'))[5].find('table').table.find_all('tr')[5].find_all('td')[1].text)

    direccion.append(list(soup.find('table'))[5].find('table').table.find_all('tr')[6].find_all('td')[1].text)

    info_completa = pd.DataFrame({
        'Cedula': cedula,
        'Nombre': nombre,
        'Estado': estado,
        'Municipio': municipio,
        'Parroquia': parroquia,
        'Centro': centro,
        'Direccion': direccion
    })
    # info_completa.to_csv('cne.csv', index=False, encoding='utf-8')
    print(info_completa)
else:
    print('El usuario no se encuentra registrado en el sistema')