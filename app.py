from flask import Flask, Blueprint
from flask_restx import Api
from flask_cors import CORS

app = Flask(__name__)

authorizations = {
    'apikey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization',
        'description': "Type in the *'Value'* input box below: **'Bearer &lt;JWT&gt;'**, where JWT is the token"
    }
}

# swagger route kind of thing
blueprint = Blueprint('SMSApi', __name__, url_prefix='/api/v1')

CORS(app)

api = Api(blueprint, title='SMSAPI', description='This is a contact us SMSAPI', version='1.0', author='Ribiro',
          contact_email='ribirodenis05@gmail.com', doc='/doc')
app.register_blueprint(blueprint)

from controller.smsController import ns_sms

api.add_namespace(ns_sms)