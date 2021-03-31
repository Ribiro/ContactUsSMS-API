from flask_restx import Namespace, fields


class SMS:
    ns_sms = Namespace('sms', description='Use this endpoint to send a message')
    sms_model = ns_sms.model('SMS', {
        'username': fields.String(required=True, description='Your africastalking username'),
        'api_key': fields.String(required=True, description='Your api key'),
        'name': fields.String(required=True, description='Your full name'),
        'email': fields.String(required=True, description='Your email'),
        'phone': fields.String(required=True, description='Your phone number'),
        'company': fields.String(required=True, description='Your company'),
        'message': fields.String(required=True, description='Your message'),
        'recipient1': fields.String(required=True, description='recipient 1'),
        'recipient2': fields.String(required=False, description='recipient 2'),

    })
