from marshmallow import Schema, fields, validate


# "This class defines the input schema for the CreateSignup mutation. It requires a username, email,
# and password. The username must be at least 4 characters long, and the password must be at least 6
# characters long."
#
# The input schema is used to validate the input data before it is passed to the mutation
class CreateUserInputSchema(Schema):
    # the 'required' argument ensures the field exists
    first_name = fields.Str(required=True, validate=validate.Length(min=2))
    last_name = fields.Str(required=True, validate=validate.Length(min=2))
    username = fields.Str(required=True, validate=validate.Length(min=2))
    email = fields.Email(required=False)
    phone_number = fields.Str(required=False)
    age = fields.Integer(required=True)


class EditUserInputSchema(Schema):
    # the 'required' argument ensures the field exists
    # the 'required' argument ensures the field exists
    first_name = fields.Str(required=False, validate=validate.Length(min=2))
    last_name = fields.Str(required=False, validate=validate.Length(min=2))
    username = fields.Str(required=False, validate=validate.Length(min=2))
    email = fields.Email(required=False)
    phone_number = fields.Str(required=False)
    age = fields.Integer(required=False)
    