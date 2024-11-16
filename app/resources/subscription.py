from flask_restful import Resource, reqparse
from ..models import Subscription
from ..schemas import SubscriptionSchema
from .. import db

subscription_schema = SubscriptionSchema()
subscriptions_schema = SubscriptionSchema(many=True)

class SubscriptionResource(Resource):
    def get(self, user_id, category_id):
        subscription = Subscription.query.filter_by(user_id=user_id, category_id=category_id).first_or_404()
        return subscription_schema.dump(subscription), 200

    def delete(self, user_id, category_id):
        subscription = Subscription.query.filter_by(user_id=user_id, category_id=category_id).first_or_404()
        db.session.delete(subscription)
        db.session.commit()
        return {"message": "Subscription deleted successfully"}, 204

class SubscriptionListResource(Resource):
    def get(self):
        subscriptions = Subscription.query.all()
        return subscriptions_schema.dump(subscriptions), 200

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('user_id', type=int, required=True)
        parser.add_argument('category_id', type=int, required=True)
        data = parser.parse_args()

        new_subscription = Subscription(**data)
        db.session.add(new_subscription)
        db.session.commit()
        return subscription_schema.dump(new_subscription), 201
