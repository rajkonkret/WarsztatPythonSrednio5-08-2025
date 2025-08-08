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

    def __repr__(self):
        return f'{self.name}'


# tworzenie tabel
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
sesion = Session()

person = Person(name="Radek", age="23")
sesion.add(person)  # INSERT INTO person (name, age) VALUES (?, ?)
sesion.commit()

# SELECT person.id AS person_id, person.name AS person_name, person.age AS person_age
# FROM person
persons = sesion.query(Person).all()
print(persons)
# [<__main__.Person object at 0x00000235A721D590>, <__main__.Person object at 0x00000235A7182A50>]
# [Radek, Radek, Radek, Radek] dla __repr__

for p in persons:
    print(p.name)
