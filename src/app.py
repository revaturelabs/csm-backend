import atexit
from flask import Flask
from flask_restplus import Api, Resource
from apscheduler.schedulers.background import BackgroundScheduler
from src.router.batches import BatchRoute
from src.router.employees import EmployeeRoute, EmployeeManagerRoute, EmployeeIdRoute, \
                                 EmployeeIdEvaluationsRoute, swot_fields, swot_item
from src.router.categories import CategoryRoute
from src.data.associates_db import create_associates_from_scheduler
api = Api() # Initialize an instance of the Flask RestPLUS API class
app = Flask(__name__) # Initialize Flask

#Initialize the scheduler
scheduler = BackgroundScheduler()
scheduler.add_job(func=create_associates_from_scheduler, trigger="cron", day_of_week='wed', hour=11, minute=2)
scheduler.start()
atexit.register(lambda: scheduler.shutdown())

#Initialize and run the API
api.init_app(app, version='0.0', title='Caliber Staging Module Backend',
             description='The back end for the Caliber Staging Module')

''' Importing api models for documentation and validation. '''
api.models[swot_item.name] = swot_item
api.models[swot_fields.name] = swot_fields
''' Importing all the api routes. '''
api.add_resource(BatchRoute, '/batches')
api.add_resource(EmployeeRoute, '/employees')
api.add_resource(CategoryRoute, '/categories')
api.add_resource(EmployeeManagerRoute, '/employees/manager/<string:manager_id>')
api.add_resource(EmployeeIdRoute, '/employees/<string:user_id>')
api.add_resource(EmployeeIdEvaluationsRoute,
                 '/employees/<string:user_id>/evaluations')
