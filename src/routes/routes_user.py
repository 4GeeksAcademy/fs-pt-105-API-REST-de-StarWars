from flask import Blueprint, jsonify, request
from models.User import User
from database.db import db

api_user = Blueprint('api_user', __name__)

@api_user.route('/user', methods=['POST'])
def find_or_create_user():
    data = request.get_json()
    email = data.get("email")

    if not email:
        return jsonify({"error": "Email requerido"}), 400

    user = User.query.filter_by(email=email).first()

    if user:
        return jsonify({
            "message": "Usuario encontrado",
            "user": user.serialize()
        }), 200

    user = User(
        email=email,
        is_active=True
    )
    db.session.add(user)
    db.session.commit()

    return jsonify({
        "message": "Usuario creado",
        "user": user.serialize()
    }), 201