"""
Tom O'Leary
Full Stack Coffee_Shop
api.py
"""

import os
from flask import Flask, request, jsonify, abort
from sqlalchemy import exc
import json
from flask_cors import CORS

from .database.models import db_drop_and_create_all, setup_db, Drink
from .auth.auth import AuthError, requires_auth

app = Flask(__name__)
db = setup_db(app)
CORS(app)

# Initialize Database
db_drop_and_create_all()

# ROUTES
'''
GET /drinks
    public endpoint
    returns status code 200 and json {"success": True, "drinks": drinks} where drinks is the list of drinks
        or appropriate status code indicating reason for failure
'''


@app.route('/drinks', methods=['GET'])
def get_drinks():
    return jsonify({
        "success": True,
        "drinks": [drink.short() for drink in Drink.query.all()]
    }), 200


'''
GET /drinks-detail
    requires the 'get:drinks-detail' permission
    returns status code 200 and json {"success": True, "drinks": drinks} where drinks is the list of drinks
        or appropriate status code indicating reason for failure
'''


@app.route('/drinks-detail', methods=['GET'])
@requires_auth('get:drinks-detail')
def drinks_detail(jwt):
    return jsonify({
        "success": True,
        "drinks": [drink.long() for drink in Drink.query.all()]
    }), 200


'''
POST /drinks
    creates a new row in the drinks table
    requires the 'post:drinks' permission
    returns status code 200 and json {"success": True, "drinks": drink} where drink an array containing only the newly created drink
        or appropriate status code indicating reason for failure
'''


@app.route('/drinks', methods=['POST'])
@requires_auth('post:drinks')
def add_drinks(jwt):
    data = request.json
    drink = Drink(title=data.get('title'),
                  recipe=data.get('recipe') if type(data.get('recipe')) == str
                  else json.dumps(data.get('recipe')))
    try:
        drink.insert()
        return jsonify({
            'success': True,
            'drink': drink.long()
        }), 200
    except():
        return jsonify({
            'success': False,
            'error': "Internal Error"
        }), 500


'''
PATCH /drinks/<id>
    where <id> is the existing model id
    responds with a 404 error if <id> is not found
    updates the corresponding row for <id>
    requires the 'patch:drinks' permission
    returns status code 200 and json {"success": True, "drinks": drink} where drink an array containing only the updated drink
        or appropriate status code indicating reason for failure
'''


@app.route('/drinks/<id>', methods=['PATCH'])
@requires_auth('patch:drinks')
def edit_drinks(jwt, id):
    try:
        data = request.json
        drink = Drink.query.filter(Drink.id == id).one_or_none()

        if drink:
            if data.get('title'):
                drink.title = data.get('title')
            else:
                drink.title = drink.title

            if data.get('recipe'):
                recipe = data.get('recipe')
            else:
                recipe = drink.recipe

            if type(recipe) == str:
                drink.recipe = recipe
            else:
                json.dumps(recipe)

            drink.update()

            return jsonify({
                "success": True,
                "drinks": [drink.long()]
            }), 200
    except():
        return jsonify({
            "success": False,
            "error": "id: " + id + " Not Found"
        }), 404

'''
DELETE /drinks/<id>
    where <id> is the existing model id
    responds with a 404 error if <id> is not found
    deletes the corresponding row for <id>
    requires the 'delete:drinks' permission
    returns status code 200 and json {"success": True, "delete": id} where id is the id of the deleted record
        or appropriate status code indicating reason for failure
'''


@app.route('/drinks/<id>', methods=['DELETE'])
@requires_auth('delete:drinks')
def delete_drinks(jwt, id):
    try:
        drink = Drink.query.filter(Drink.id == id).one_or_none()

        if drink:
            drink.delete()

            return jsonify({
                "success": True,
                "delete": id
            }), 200
    except():
        return jsonify({
            "success": False,
            "error": "id: " + id + " Not Found"
        }), 404


# Error Handling
@app.errorhandler(422)
def unprocessable(error):
    return jsonify({
        "success": False,
        "error": 422,
        "message": "unprocessable"
    }), 422


@app.errorhandler(404)
def unprocessable(error):
    return jsonify({
        "success": False,
        "error": 404,
        "message": "resource not found"
    }), 404


@app.errorhandler(AuthError)
def handle_auth_error(e):
    res = jsonify(e.error)
    res.status_code = e.status_code
    return res
