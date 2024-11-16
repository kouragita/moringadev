from flask_restful import Resource, reqparse
from flask import jsonify
from ..models import Content
from ..schemas import ContentSchema
from .. import db

content_schema = ContentSchema()
contents_schema = ContentSchema(many=True)

class ContentResource(Resource):
    def get(self, content_id):
        content = Content.query.get_or_404(content_id)
        return content_schema.dump(content), 200

    def delete(self, content_id):
        content = Content.query.get_or_404(content_id)
        db.session.delete(content)
        db.session.commit()
        return {"message": "Content deleted successfully"}, 204

class ContentListResource(Resource):
    def get(self):
        contents = Content.query.all()
        return contents_schema.dump(contents), 200

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('title', required=True)
        parser.add_argument('type', required=True)
        parser.add_argument('category_id', type=int, required=True)
        parser.add_argument('author_id', type=int, required=True)
        parser.add_argument('is_approved', type=bool, default=False)
        data = parser.parse_args()

        new_content = Content(**data)
        db.session.add(new_content)
        db.session.commit()
        return content_schema.dump(new_content), 201
