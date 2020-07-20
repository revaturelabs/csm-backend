import atexit
from flask import Flask
from flask_restplus import Api, Resource
from apscheduler.schedulers.background import BackgroundScheduler
from src.router.batches import BatchRoute
from src.router.employees import EmployeeRoute, EmployeeManagerRoute, EmployeeIdRoute, EmployeeIdEvaluationsRoute
from src.router.categories import CategoryRoute

api = Api() # Initialize an instance of the Flask RestPLUS API class
app = Flask(__name__) # Initialize Flask

#Initialize the scheduler
scheduler = BackgroundScheduler()
scheduler.add_job(func='''NAME OF THE FUNCTION TO RUN''', trigger="cron", day_of_week='fri')
scheduler.start()
atexit.register(lambda: scheduler.shutdown())

#Initialize and run the API
api.init_app(app, version='0.0', title='Caliber Staging Module Backend',
             description='The back end for the Caliber Staging Module')

api.add_resource(BatchRoute, '/batches')
api.add_resource(EmployeeRoute, '/employees')
api.add_resource(CategoryRoute, '/categories')
api.add_resource(EmployeeManagerRoute, '/employees/manager/<string:manager_id>')
api.add_resource(EmployeeIdRoute, '/employees/<string:user_id>')
api.add_resource(EmployeeIdEvaluationsRoute, '/employees/<string:batch_id>/evaluations/<string:user_id>')

@api.route('/api') # Route declaration
@api.doc() # Documentation decorator
class ApiRoute(Resource):

    @api.response(200, 'Success')
    def get(self):
        return { "status": "You got me!" }
