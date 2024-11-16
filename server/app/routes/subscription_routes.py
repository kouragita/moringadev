from flask import request, jsonify, abort
from app.models import db
from app.models.subscription import Subscription 
from app.schemas.subscription_schema import SubscriptionSchema
from . import main

subscription_schema = SubscriptionSchema()
subscriptions_schema = SubscriptionSchema(many=True)

@main.route('/subscriptions', methods=['POST'])
def create_subscription():
    json_data = request.get_json()
    subscription_data = subscription_schema.load(json_data)
    subscription = Subscription(**subscription_data)
    db.session.add(subscription)
    db.session.commit()
    return subscription_schema.dump(subscription), 201

@main.route('/subscriptions', methods=['GET'])
def get_subscriptions():
    subscriptions = Subscription.query.all()
    return subscriptions_schema.dump(subscriptions), 200

@main.route('/subscriptions/<int:subscription_id>', methods=['GET'])
def get_subscription(subscription_id):
    subscription = Subscription.query.get(subscription_id)
    if subscription is None:
        abort(404)
    return subscription_schema.dump(subscription), 200

@main.route('/subscriptions/<int:subscription_id>', methods=['PUT'])
def update_subscription(subscription_id):
    subscription = Subscription.query.get(subscription_id)
    if subscription is None:
        abort(404)

    json_data = request.get_json()
    subscription_data = subscription_schema.load(json_data)
    for key, value in subscription_data.items():
        setattr(subscription, key, value)
    db.session.commit()
    return subscription_schema.dump(subscription), 200

@main.route('/subscriptions/<int:subscription_id>', methods=['DELETE'])
def delete_subscription(subscription_id):
    subscription = Subscription.query.get(subscription_id)
    if subscription is None:
        abort(404)

    db.session.delete(subscription)
    db.session.commit()
    return '', 204