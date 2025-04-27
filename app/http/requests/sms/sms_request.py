from marshmallow import Schema, fields


class SmsSchema(Schema):
 
    phone_number = fields.Integer(required=True)
    user_id = fields.Integer(required=False)