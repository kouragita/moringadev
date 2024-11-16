from flask import request, jsonify, abort
from app.models import db
from app.models.category import Category
from app.schemas.category_schema import CategorySchema
from . import main

category_schema = CategorySchema()
categories_schema = CategorySchema(many=True)

@main.route('/categories', methods=['POST'])
def create_category():
    json_data = request.get_json()
    category_data = category_schema.load(json_data)
    category = Category(**category_data)
    db.session.add(category)
    db.session.commit()
    return category_schema.dump(category), 201

@main.route('/categories', methods=['GET'])
def get_categories():
    categories = Category.query.all()
    return categories_schema.dump(categories), 200

@main.route('/categories/<int:category_id>', methods=['GET'])
def get_category(category_id):
    category = Category.query.get(category_id)
    if category is None:
        abort(404)
    return category_schema.dump(category), 200

@main.route('/categories/<int:category_id>', methods=['PUT'])
def update_category(category_id):
    category = Category.query.get(category_id)
    if category is None:
        abort(404)

    json_data = request.get_json()
    category_data = category_schema.load(json_data)
    for key, value in category_data.items():
        setattr(category, key, value)
    db.session.commit()
    return category_schema.dump(category), 200

@main.route('/categories/<int:category_id>', methods=['DELETE'])
def delete_category(category_id):
    category = Category.query.get(category_id)
    if category is None:
        abort(404)

    db.session.delete(category)
    db.session.commit()
    return '', 204