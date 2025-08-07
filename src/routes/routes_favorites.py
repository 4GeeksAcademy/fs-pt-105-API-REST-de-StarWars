from flask import Blueprint, jsonify, request
from models.Favorite import Favorite
from models.People import People
from models.Planet import Planet
from database.db import db

api_favorites = Blueprint('api_favorites', __name__)

# Ver favoritos de un usuario
@api_favorites.route('/users/favorites', methods=['GET'])
def get_user_favorites():
    user_id = request.args.get("user_id")
    if not user_id:
        return jsonify({"error": "User ID is required"}), 400

    favorites = Favorite.query.filter_by(user_id=user_id).all()
    result = []

    for fav in favorites:
        if fav.people_id:
            person = People.query.get(fav.people_id)
            result.append({"type": "people", "data": person.serialize()})
        elif fav.planet_id:
            planet = Planet.query.get(fav.planet_id)
            result.append({"type": "planet", "data": planet.serialize()})

    return jsonify(result), 200

# Añadir favoritos
@api_favorites.route('/favorite/planet/<int:planet_id>', methods=['POST'])
def add_fav_planet(planet_id):
    user_id = request.json.get("user_id")
    if not user_id:
        return jsonify({"error": "User ID is required"}), 400

    fav = Favorite(user_id=user_id, planet_id=planet_id)
    db.session.add(fav)
    db.session.commit()
    return jsonify(fav.serialize()), 201

@api_favorites.route('/favorite/people/<int:people_id>', methods=['POST'])
def add_fav_people(people_id):
    user_id = request.json.get("user_id")
    if not user_id:
        return jsonify({"error": "User ID is required"}), 400

    fav = Favorite(user_id=user_id, people_id=people_id)
    db.session.add(fav)
    db.session.commit()
    return jsonify(fav.serialize()), 201

# Eliminar favoritos
@api_favorites.route('/favorite/planet/<int:planet_id>', methods=['DELETE'])
def delete_fav_planet(planet_id):
    user_id = request.args.get("user_id")
    fav = Favorite.query.filter_by(user_id=user_id, planet_id=planet_id).first()
    if fav:
        db.session.delete(fav)
        db.session.commit()
        return jsonify({"message": "Deleted"}), 200
    return jsonify({"error": "Not found"}), 404

@api_favorites.route('/favorite/people/<int:people_id>', methods=['DELETE'])
def delete_fav_people(people_id):
    user_id = request.args.get("user_id")
    fav = Favorite.query.filter_by(user_id=user_id, people_id=people_id).first()
    if fav:
        db.session.delete(fav)
        db.session.commit()
        return jsonify({"message": "Deleted"}), 200
    return jsonify({"error": "Not found"}), 404