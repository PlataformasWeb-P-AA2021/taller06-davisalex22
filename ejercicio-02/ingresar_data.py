from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import requests
from generar_base import Pais

import json

# se genera en enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine('sqlite:///basepaises.db')


Session = sessionmaker(bind=engine)
session = Session()

paises = requests.get('https://pkgstore.datahub.io/core/country-codes/country-codes_json/data/616b1fb83cbfd4eb6d9e7d52924bb00a/country-codes_json.json')
datos_json = json.loads(paises.content)

# print(datos_json)
#documentos = ar_json["docs"]
print(datos_json)
for d in datos_json:
    print(d)
    p = Pais(nombrePais=d['CLDR display name'], capital=d['Capital'], continente=d['Continent'], \
            dial=d['Dial'], geonameID=d['Geoname ID'], itu=d['ITU'], lenguajes=d['Languages'], dependencia=d['is_independent'])
    session.add(p)

# confirmar transacciones
session.commit()