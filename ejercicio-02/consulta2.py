from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_ # se importa el operador and

# se importa la clase(s) del 
# archivo genera_tablas
from generar_base import Pais 

engine = create_engine('sqlite:///basepaises.db')

Session = sessionmaker(bind=engine)
session = Session()

#Presentar los países de Asía, ordenados por el atributo Dial.
consulta2 = session.query(Pais).filter(Pais.continente=="AS").order_by(Pais.dial).all()
print(consulta2)