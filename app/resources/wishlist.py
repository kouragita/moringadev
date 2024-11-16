from flask_restful import Resource, reqparse
from app.models import Wishlist
from app.schemas import WishlistSchema
from app.models import db

wishlist_schema = WishlistSchema()
wishlists_schema = WishlistSchema(many=True)

class WishlistResource(Resource):
    def get(self, wishlist_id):
        wishlist = Wishlist.query.get_or_404(wishlist_id)
        return wishlist_schema.dump(wishlist), 200

    def delete(self, wishlist_id):
        wishlist = Wishlist.query.get_or_404(wishlist_id)
        db.session.delete(wishlist)
        db.session.commit()
        return {"message": "Wishlist entry deleted successfully"}, 204

class WishlistListResource(Resource):
    def get(self):
        wishlists = Wishlist.query.all()
        return wishlists_schema.dump(wishlists), 200

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('user_id', type=int, required=True)
        parser.add_argument('content_id', type=int, required=True)
        data = parser.parse_args()

        new_wishlist = Wishlist(**data)
        db.session.add(new_wishlist)
        db.session.commit()
        return wishlist_schema.dump(new_wishlist), 201
