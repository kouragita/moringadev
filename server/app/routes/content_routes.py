from flask import request, jsonify, abort
from app.models import db 
from app.models.content import Content
from app.schemas.content_schema import ContentSchema
from . import main

content_schema = ContentSchema()
contents_schema = ContentSchema(many=True)

@main.route('/contents', methods=['POST'])
def create_content():
    json_data = request.get_json()
    content_data = content_schema.load(json_data)
    content = Content(**content_data)
    db.session.add(content)
    db.session.commit()
    return content_schema.dump(content), 201

@main.route('/contents', methods=['GET'])
def get_contents():
    contents = Content.query.all()
    return contents_schema.dump(contents), 200

@main.route('/contents/<int:content_id>', methods=['GET'])
def get_content(content_id):
    content = Content.query.get(content_id)
    if content is None:
        abort(404)
    return content_schema.dump(content), 200

@main.route('/contents/<int:content_id>', methods=['PUT'])
def update_content(content_id):
    content = Content.query.get(content_id)
    if content is None:
        abort(404)

    json_data = request.get_json()
    content_data = content_schema.load(json_data)
    for key, value in content_data.items():
        setattr(content, key, value)
    db.session.commit()
    return content_schema.dump(content), 200

@main.route('/contents/<int:content_id>', methods=['DELETE'])
def delete_content(content_id):
    content = Content.query.get(content_id)
    if content is None:
        abort(404)

    db.session.delete(content)
    db.session.commit()
    return '', 204