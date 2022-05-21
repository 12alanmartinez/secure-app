"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User, Characters, planets
from api.utils import generate_sitemap, APIException
from flask_jwt_extended import create_access_token, jwt_required
api = Blueprint('api', __name__)


@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    }

    return jsonify(response_body), 200


@api.route('/register', methods=['post'])
def register():
    payload = request.get_json()

    user = User(email=payload['email'],
                password=payload['password'],
                is_active=True
                )

    db.session.add(user)
    db.session.commit()

    return "user registered", 200


@api.route('/login', methods=['post'])
def login():
    payload = request.get_json()

    user = User.query.filter(User.email == payload['email']).first()
    if user is None:
        return "failed-auth", 401

    if user.password != payload['password']:
        return 'failed-auth', 401

    token = create_access_token(identity=user.id)

    return jsonify({'token': token})


@api.route('/accounts', methods=['GET'])
@jwt_required()
def accounts():
    User_id = get_jwt_identity()

    user = User.query.get(User_id)
    account_info = {
        "accounts": [
            {"accounts": "009001", "total": "$100.00"},
            {"accounts": "0009002", "total": "$5000.65"},
        ],
        "user": user.serialize()
    }

    return jsonify(account_info)


@api.route('/characters', methods=['GET'])
@
