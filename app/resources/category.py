from flask_restful import Resource, reqparse
from ..models import Category
from ..schemas import CategorySchema
from .. import db

category_schema = CategorySchema()
categories_schema = CategorySchema(many=True)

class CategoryResource(Resource):
    def get(self, category_id):
        category = Category.query.get_or_404(category_id)
        return category_schema.dump(category), 200

    def delete(self, category_id):
        category = Category.query.get_or_404(category_id)
        db.session.delete(category)
        db.session.commit()
        return {"message": "Category deleted successfully"}, 204

class CategoryListResource(Resource):
    def get(self):
        categories = Category.query.all()
        return categories_schema.dump(categories), 200

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', required=True)
        data = parser.parse_args()

        new_category = Category(**data)
        db.session.add(new_category)
        db.session.commit()
        return category_schema.dump(new_category), 201
