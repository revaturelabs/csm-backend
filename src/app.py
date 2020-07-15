from flask import Flask
from flask_restplus import Api, Resource
from router.batches import BatchRoute
from router.employees import EmployeeRoute, EmployeeManagerRoute, EmployeeIdRoute, EmployeeIdEvaluationsRoute
from router.categories import CategoryRoute

api = Api() # Initialize an instance of the Flask RestPLUS API class
app = Flask(__name__) # Initialize Flask

# Initialize and run the API
api.init_app(app, version='0.0', title='Caliber Staging Module Backend',
             description='The back end for the Caliber Staging Module')

api.add_resource(BatchRoute, '/batches')
api.add_resource(EmployeeRoute, '/employees')
api.add_resource(CategoryRoute, '/categories')
api.add_resource(EmployeeManagerRoute, '/employees/manager/<str:manager_id>')
api.add_resource(EmployeeIdRoute, '/employees/<str:user_id>')
api.add_resource(EmployeeIdEvaluationsRoute, '/employees/<str:user_id>/evaluations')



@api.route('/api') # Route declaration
@api.doc() # Documentation decorator
class ApiRoute(Resource):

    @api.response(200, 'Success')
    def get(self):
        return { "status": "You got me!" }
