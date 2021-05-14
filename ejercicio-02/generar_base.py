from sqlalchemy import create_engine

# se genera en enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine('sqlite:///basepaises.db')

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


from sqlalchemy import Column, Integer, String

class Pais(Base):
    __tablename__ = 'paises'
    
    id = Column(Integer, primary_key=True)
    nombrePais = Column(String)
    capital = Column(String)
    continente = Column(String)
    dial = Column(String)
    geonameID = Column(Integer)
    itu = Column(String)
    lenguajes = Column(String)
    dependencia = Column(String)

    def __repr__(self):
            return "Pais: nombrePais = %s capital = %s continente = %s dial = %s geonameID = %s itu = %s lenguajes = %s dependencia: %s \n" % (
                            self.nombrePais, 
                            self.capital, 
                            self.continente,
                            self.dial,
                            self.geonameID,
                            self.itu,
                            self.lenguajes,
                            self.dependencia)
    

Base.metadata.create_all(engine)

