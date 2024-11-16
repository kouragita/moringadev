from marshmallow import ValidationError

def validate_user_data(data, schema):
    try:
        schema.load(data)
    except ValidationError as err:
        return err.messages
    return None