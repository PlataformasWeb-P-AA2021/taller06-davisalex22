from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_ # se importa el operador and

# se importa la clase(s) del 
# archivo genera_tablas
from generar_base import Pais 

engine = create_engine('sqlite:///basepaises.db')

Session = sessionmaker(bind=engine)
session = Session()

#Presentar todos los países que tengan en su cadena de nombre de país "uador" o en su cadena de capital "ito".
consulta5 = session.query(Pais).filter(or_(Pais.nombrePais.like("%uador%"), Pais.capital.like("%ito%"))).all() 
 
print(consulta5)