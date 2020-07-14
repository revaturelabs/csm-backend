from flask import Flask
from flask_restplus import Api, Resource
import requests

r = requests.get('https://pokeapi.co/api/v2/pokemon/ditto')
print(r.json())

api = Api()
app = Flask(__name__)

api.init_app(app, version='0.0', title='Caliber Staging Module Backend',
             description='The back end for the Caliber Staging Module')

@api.route('/api')
@api.doc()
class ApiRoute(Resource):

    @api.response(200, 'Success')
    def get(self):
        return { "status": "You got me!" }
