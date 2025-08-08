# Mapowanie obiektowo-relacyjne (ang. Object-Relational Mapping – ORM) – sposób odwzorowania obiektowej architektury systemu informatycznego
# na bazę danych (lub inny element systemu) o relacyjnym charakterze.
# pip install sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import relationship, sessionmaker, declarative_base

# echo=Truebedziemy widziec komendy sql
engine = create_engine('sqlite:///moja_baza.db', echo=True)
Base = declarative_base()


# model, encja - klasa odwzorowująca tabelę w bazie danych
class Person(Base):
    __tablename__ = "person"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(String)


# tworzenie tabel
Base.metadata.create_all(engine)
