from flask_restx import Resource
from utils.smsUtil import SMS

import africastalking

ns_sms = SMS.ns_sms
sms_model = SMS.sms_model


@ns_sms.route('')
class SMS(Resource):
    @ns_sms.expect(sms_model)
    def post(self):
        """Use this endpoint to send a new sms"""
        data = ns_sms.payload

        africastalking.initialize(data['username'], data['api_key'])

        # Initialize a service e.g. SMS
        sms = africastalking.SMS

        code = '+254'

        recipient1 = data['recipient1']
        recipient1 = code + recipient1[1:]

        recipient2 = data['recipient2']
        recipient2 = code + recipient2[1:]

        # Use the service synchronously
        response = sms.send('Name:' + data['name'] + '. Email:' + data['email'] + '. ' + 'Phone:' + data['phone']
                            + '. Company:' + data['company'] + '. Message:' + data['message'], [recipient1, recipient2])

        return response['Recipients']
