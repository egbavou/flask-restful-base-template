from marshmallow import Schema, fields, validate

class RegisterSchema(Schema):
    
    first_name = fields.String(required=True,validate=validate.Length(min=1,max=255))
    last_name = fields.String(required=False,validate=validate.Length(max=255))
    birth_date = fields.Date(format='%Y-%m-%d',required=True)
    username = fields.String(required=True,validate=[validate.Length(min=1,max=255),validate.Regexp(regex="^[a-zA-Z0-9_.-]*$")])
    email = fields.Email(required=True)
    password = fields.String(required=True,validate=validate.Length(min=8,max=255))
    device_id = fields.String(required=False,allow_none=True)
    hardware_device_id = fields.String(required=False,allow_none=True)
    
    # @validates_schema
    # def validate_username(self, data, **kwargs):
    #     if data['username'].find('/[\'^£$%&*()}ÀàÁáÂâÃãÄäÅåÆæÇçÐðÈèÉéÊêËëÌìÍíÎîÏïÑñÒòÓóÔôÕõÖöœŒØøßÙùÚúÛûÜüÝýÞþŸÿ{@#~?><>,|=+¬]/') != -1:
    #         raise ValidationError('Invalid Username')
    
class EmailSchema(Schema):
 
    email = fields.Email(required=True,validate=validate.Length(min=1,max=255))
    
class UsernameSchema(Schema):

    username = fields.String(
        required=True,
        validate=[
            validate.Length(min=1,max=255),
            validate.Regexp(regex="^[a-zA-Z0-9_.-]*$")
        ]
    )
    hardware_device_id = fields.String(required=False,allow_none=True)