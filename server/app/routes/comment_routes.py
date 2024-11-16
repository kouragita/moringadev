from flask import request, jsonify, abort
from app.models import db
from app.models.comment import Comment
from app.schemas.comment_schema import CommentSchema
from . import main

comment_schema = CommentSchema()
comments_schema = CommentSchema(many=True)

@main.route('/comments', methods=['POST'])
def create_comment():
    json_data = request.get_json()
    comment_data = comment_schema.load(json_data)
    comment = Comment(**comment_data)
    db.session.add(comment)
    db.session.commit()
    return comment_schema.dump(comment), 201

@main.route('/comments', methods=['GET'])
def get_comments():
    comments = Comment.query.all()
    return comments_schema.dump(comments), 200

@main.route('/comments/<int:comment_id>', methods=['GET'])
def get_comment(comment_id):
    comment = Comment.query.get(comment_id)
    if comment is None:
        abort(404)
    return comment_schema.dump(comment), 200

@main.route('/comments/<int:comment_id>', methods=['PUT'])
def update_comment(comment_id):
    comment = Comment.query.get(comment_id)
    if comment is None:
        abort(404)

    json_data = request.get_json()
    comment_data = comment_schema.load(json_data)
    for key, value in comment_data.items():
        setattr(comment, key, value)
    db.session.commit()
    return comment_schema.dump(comment), 200

@main.route('/comments/<int:comment_id>', methods=['DELETE'])
def delete_comment(comment_id):
    comment = Comment.query.get(comment_id)
    if comment is None:
        abort(404)

    db.session.delete(comment)
    db.session.commit()
    return '', 204