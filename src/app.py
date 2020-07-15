from flask import Flask
from flask_restplus import Api, Resource
from src.router.batches import BatchRoute

api = Api() # Initialize an instance of the Flask RestPLUS API class
app = Flask(__name__) # Initialize Flask

# Initialize and run the API
api.init_app(app, version='0.0', title='Caliber Staging Module Backend',
             description='The back end for the Caliber Staging Module')

api.add_resource(BatchRoute, '/test')

@api.route('/api') # Route declaration
@api.doc() # Documentation decorator
class ApiRoute(Resource):

    @api.response(200, 'Success')
    def get(self):
        return { "status": "You got me!" }
