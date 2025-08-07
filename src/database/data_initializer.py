from database.db import db
from models.Planet import Planet
from models.Person import Person
from models.User import User
from app import app  

def load_initial_data():
    with app.app_context():
        # Limpia tablas 
        Planet.query.delete()
        Person.query.delete()
        User.query.delete()
        db.session.commit()

        # Crea planetas
        planets = [
            Planet(name="Tatooine", climate="arid", terrain="desert", population="200000"),
            Planet(name="Alderaan", climate="temperate", terrain="grasslands, mountains", population="2000000000"),
            Planet(name="Hoth", climate="frozen", terrain="tundra, ice caves, mountain ranges", population="unknown"),
        ]
        db.session.bulk_save_objects(planets)

        
        people = [
            Person(name="Luke Skywalker", gender="male", height="172", mass="77", birth_year="19BBY", skin_color="fair", eye_color="blue", hair_color="blond"),
            Person(name="Darth Vader", gender="male", height="202", mass="136", birth_year="41.9BBY", skin_color="white", eye_color="yellow", hair_color="none"),
            Person(name="Leia Organa", gender="female", height="150", mass="49", birth_year="19BBY", skin_color="light", eye_color="brown", hair_color="brown"),
        ]
        db.session.bulk_save_objects(people)

        # Crea usuarios 
        user = User(email="admin@example.com", is_active=True)
        db.session.add(user)

        db.session.commit()
        print("Datos iniciales cargados correctamente.")

if __name__ == "__main__":
    load_initial_data()