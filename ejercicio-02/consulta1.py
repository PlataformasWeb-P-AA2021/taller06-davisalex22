from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_ # se importa el operador and

# se importa la clase(s) del 
# archivo genera_tablas
from generar_base import Pais

# se genera enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite

engine = create_engine('sqlite:///basepaises.db')

Session = sessionmaker(bind=engine)
session = Session()


# Presentar todos los países del continente americano
consulta1 = session.query(Pais).filter(Pais.continente=="NA").all()
print(consulta1)