from flask_restful import Resource, reqparse
from ..models import Comment
from ..schemas import CommentSchema
from .. import db

comment_schema = CommentSchema()
comments_schema = CommentSchema(many=True)

class CommentResource(Resource):
    def get(self, comment_id):
        comment = Comment.query.get_or_404(comment_id)
        return comment_schema.dump(comment), 200

    def delete(self, comment_id):
        comment = Comment.query.get_or_404(comment_id)
        db.session.delete(comment)
        db.session.commit()
        return {"message": "Comment deleted successfully"}, 204

class CommentListResource(Resource):
    def get(self):
        comments = Comment.query.all()
        return comments_schema.dump(comments), 200

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('content_id', type=int, required=True)
        parser.add_argument('user_id', type=int, required=True)
        parser.add_argument('comment_text', required=True)
        parser.add_argument('parent_comment_id', type=int, default=None)
        data = parser.parse_args()

        new_comment = Comment(**data)
        db.session.add(new_comment)
        db.session.commit()
        return comment_schema.dump(new_comment), 201
