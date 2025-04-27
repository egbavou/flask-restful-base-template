from marshmallow import Schema, fields, validate, ValidationError, validates_schema

class SendResetPasswordCodeSchema(Schema):
    
    email = fields.Email(required=False)
    phone_number = fields.String(required=False)
    
    @validates_schema
    def validate_email_or_phone_number(self, data, **kwargs):
        if data.get('email') is None and data.get('phone_number') is None: 
            raise ValidationError("The phone number field is required when email is not present.")
        
class CheckResetPasswordCodeSchema(Schema):
    
    email = fields.Email(required=False)
    phone_number = fields.String(required=False)
    code = fields.Integer(required=True)
    
    @validates_schema
    def validate_email_or_phone_number(self, data, **kwargs):
        if data.get('email') is None and data.get('phone_number') is None: 
            raise ValidationError("The phone number field is required when email is not present.")
        
class ResetPasswordSchema(Schema):
    
    email = fields.Email(required=False)
    phone_number = fields.String(required=False)
    code = fields.Integer(required=True)
    password = fields.String(required=True)
    
    @validates_schema
    def validate_email_or_phone_number(self, data, **kwargs):
        if data.get('email') is None and data.get('phone_number') is None: 
            raise ValidationError("The phone number field is required when email is not present.")
        
class VerifyEmailCodeSchema(Schema):
    
    code = fields.Integer(required=True)

class UpdateDeviceIdInputSchema(Schema):
    
    device_id = fields.Str(required=True)