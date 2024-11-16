from flask import request, jsonify, abort
from app.models import db
from app.models.wishlist import Wishlist
from app.schemas.wishlist_schema import WishlistSchema
from . import main

wishlist_schema = WishlistSchema()
wishlists_schema = WishlistSchema(many=True)

@main.route('/wishlists', methods=['POST'])
def create_wishlist():
    json_data = request.get_json()
    wishlist_data = wishlist_schema.load(json_data)
    wishlist = Wishlist(**wishlist_data)
    db.session.add(wishlist)
    db.session.commit()
    return wishlist_schema.dump(wishlist), 201

@main.route('/wishlists', methods=['GET'])
def get_wishlists():
    wishlists = Wishlist.query.all()
    return wishlists_schema.dump(wishlists), 200

@main.route('/wishlists/<int:wishlist_id>', methods=['GET'])
def get_wishlist(wishlist_id):
    wishlist = Wishlist.query.get(wishlist_id)
    if wishlist is None:
        abort(404)
    return wishlist_schema.dump(wishlist), 200

@main.route('/wishlists/<int:wishlist_id>', methods=['PUT'])  # Fixed here
def update_wishlist(wishlist_id):
    wishlist = Wishlist.query.get(wishlist_id)
    if wishlist is None:
        abort(404)

    json_data = request.get_json()
    wishlist_data = wishlist_schema.load(json_data)
    for key, value in wishlist_data.items():
        setattr(wishlist, key, value)
    db.session.commit()
    return wishlist_schema.dump(wishlist), 200

@main.route('/wishlists/<int:wishlist_id>', methods=['DELETE'])
def delete_wishlist(wishlist_id):
    wishlist = Wishlist.query.get(wishlist_id)
    if wishlist is None:
        abort(404)

    db.session.delete(wishlist)
    db.session.commit()
    return '', 204