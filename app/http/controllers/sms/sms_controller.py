from app.http.requests.sms.sms_request import SmsSchema
from app.utils.common import generate_response
from app.utils.http_code import HTTP_200_OK
import random
# from app.jobs.sms.sms_tasks import send_sms_job
# from app.jobs.graylog.graylog_tasks import send_message_to_sqs_job

def send_sms(request,input_data):
    
    validator = SmsSchema()
    errors = validator.validate(input_data)
    
    if errors:
        
        return generate_response(message=errors)
    
    code =  random.randint(10000,99999)
        
    data = {
        'code': code,
    }

    # send_sms_job.delay({
    #     'code': code,
    #     'phone_number': input_data.get('phone_number')
    # })
        
    return generate_response(
        data= data,
        message="Sms send successfully.",
        status=HTTP_200_OK
    )