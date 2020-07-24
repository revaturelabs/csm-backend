''' Entry file for backend of application '''
from flask import Flask
from flask_cors import CORS
from flask_restplus import Api
from flask_cors import CORS
from src.router.batches import BatchRoute, BatchIndividualRoute
from src.router.managers import ManagerRoute
from src.router.employees import EmployeeRoute, EmployeeManagerRoute, EmployeeIdRoute, \
                                 EmployeeIdEvaluationsRoute, swot_fields, swot_item
from src.router.categories import CategoryRoute

api = Api() # Initialize an instance of the Flask RestPLUS API class
app = Flask(__name__) # Initialize Flask
CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)

# Initialize CORS for cross origin requests for testing purposes
CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)

# Initialize and run the API
api.init_app(app, version='0.0', title='Caliber Staging Module Backend',
             description='The back end for the Caliber Staging Module')

''' Importing api models for documentation and validation. '''
api.models[swot_item.name] = swot_item
api.models[swot_fields.name] = swot_fields
''' Importing all the api routes. '''
api.add_resource(BatchRoute, '/batches')
api.add_resource(BatchIndividualRoute, '/batches/<string:batch_id>')
api.add_resource(EmployeeRoute, '/employees')
api.add_resource(CategoryRoute, '/categories')
api.add_resource(EmployeeManagerRoute, '/employees/manager/<string:manager_id>')
api.add_resource(EmployeeIdRoute, '/employees/<string:user_id>')
api.add_resource(EmployeeIdEvaluationsRoute, '/employees/<string:user_id>/evaluations')
api.add_resource(ManagerRoute, '/managers/<string:manager_id>')

