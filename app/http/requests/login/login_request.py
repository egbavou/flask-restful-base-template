from marshmallow import Schema, fields, validate ,ValidationError, validates_schema

class LoginSchema(Schema):
    
    username = fields.String(required=False,validate=[validate.Length(min=1,max=255),validate.Regexp(regex="^[a-zA-Z0-9_.-]*$")],allow_none=True)
    email = fields.Email(required=False,allow_none=True)
    type = fields.String(required=True,validate=validate.OneOf(['username','email']))
    password = fields.String(required=True,validate=validate.Length(min=8,max=255))
    device_id = fields.String(required=False,allow_none=True)
    hardware_device_id = fields.String(required=False,allow_none=True)

    
    @validates_schema
    def validate_email_or_phone_number(self, data, **kwargs):
        if data.get('email') is None and data.get('username') is None: 
            raise ValidationError("The username field is required when email is not present.")

class LogoutSchema(Schema):
    device_id = fields.Str(required=False, allow_none=True)
    hardware_device_id = fields.String(required=False, allow_none=True)