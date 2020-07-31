''' Entry file for backend of application '''
import atexit
from flask import Flask
from flask_cors import CORS
from flask_restplus import Api, Resource
from apscheduler.schedulers.background import BackgroundScheduler
from src.router.models import swot_item, swot_fields, associate_model, associate_model_short, \
                              trainer_info_model, associate_model_trainer, category_model, \
                              batch_model, associate_model_manager_view, spider_data_model, \
                              qc_note_model, associate_evaluation_model, manager_model
from src.router.batches import BatchRoute, BatchIndividualRoute
from src.router.managers import ManagerRoute
from src.router.employees import EmployeeRoute, EmployeeManagerRoute, EmployeeIdRoute, \
                                 EmployeeIdEvaluationsRoute
from src.router.categories import CategoryRoute
from src.data.associates_db import create_associates_from_scheduler
api = Api() # Initialize an instance of the Flask RestPLUS API class
app = Flask(__name__) # Initialize Flask

#Initialize the scheduler
scheduler = BackgroundScheduler()
scheduler.add_job(func=create_associates_from_scheduler, trigger="cron",
                  day_of_week='fri', hour=18)
scheduler.start()
atexit.register(lambda: scheduler.shutdown())

# Initialize CORS for cross origin requests for testing purposes
CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)

# Initialize and run the API
api.init_app(app, version='0.0', title='Caliber Staging Module Backend',
             description='The back end for the Caliber Staging Module')

# Importing api models for documentation and validation.
api.models[swot_item.name] = swot_item
api.models[swot_fields.name] = swot_fields
api.models[associate_model.name] = associate_model
api.models[associate_model_short.name] = associate_model_short
api.models[associate_model_manager_view.name] = associate_model_manager_view
api.models[associate_evaluation_model.name] = associate_evaluation_model
api.models[spider_data_model.name] = spider_data_model
api.models[qc_note_model.name] = qc_note_model
api.models[trainer_info_model.name] = trainer_info_model
api.models[associate_model_trainer.name] = associate_model_trainer
api.models[category_model.name] = category_model
api.models[batch_model.name] = batch_model
api.models[manager_model.name] = manager_model

''' Importing all the api routes. '''
api.add_resource(BatchRoute, '/batches')
api.add_resource(BatchIndividualRoute, '/batches/<string:batch_id>')
api.add_resource(EmployeeRoute, '/employees')
api.add_resource(CategoryRoute, '/categories')
api.add_resource(EmployeeManagerRoute, '/employees/manager/<string:manager_id>')
api.add_resource(EmployeeIdRoute, '/employees/<string:user_id>')
api.add_resource(EmployeeIdEvaluationsRoute, '/employees/<string:user_id>/evaluations')
api.add_resource(ManagerRoute, '/managers/<string:manager_id>')
