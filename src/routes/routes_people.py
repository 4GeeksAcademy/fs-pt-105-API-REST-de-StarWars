from flask import Blueprint, jsonify
from models.People import People

api_people = Blueprint('api_people', __name__)

@api_people.route('/people', methods=['GET'])
def get_people():
    people = People.query.all()
    return jsonify([p.serialize() for p in people]), 200

@api_people.route('/people/<int:people_id>', methods=['GET'])
def get_one_person(people_id):
    person = People.query.get_or_404(people_id)
    return jsonify(person.serialize()), 200