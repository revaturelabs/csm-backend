''' Handles employee routes  '''

import flask
from flask_restplus import Resource, Api
import src.data.associates_db as assoc_db
import src.data.swot_db as swot_db
from src.external.caliber_processing import get_qc_data, get_batch_and_associate_spider_data
from src.data.date_time_conversion import converter

from src.router.models import swot_fields, swot_item, associate_model, \
                              associate_model_manager_view, spider_data_model, qc_note_model, \
                              associate_evaluation_model

from src.logging.logger import get_logger

_log = get_logger(__name__)

api = Api()

@api.route('/employees')
class EmployeeRoute(Resource):
    '''Class for routing employee requests'''
    @api.response(200, 'Success', associate_model)
    def get(self):
        '''Retrieves a list of employees from the database '''
        emp_lst = list(assoc_db.read_all_associates())
        for i in range(0, len(emp_lst) - 1):
            if emp_lst[i]['_id'] == 'UNIQUE_COUNT':
                del emp_lst[i]
            emp_lst[i].pop('_id')
            emp_lst[i]['end_date'] = converter(emp_lst[i]['end_date'])
            if emp_lst[i]['swot']:
                for swot in emp_lst[i]['swot']:
                    swot['date_created'] = converter(swot['date_created'])
            else:
                emp_lst[i]['swot'] = [{'author': 'trainer'}]
        return emp_lst, 200

@api.route('/employees/manager/<str:manager_id>')
class EmployeeManagerRoute(Resource):
    '''Class for routing employee/manager/manager_id requests'''
    @api.response(200, 'Success', associate_model_manager_view)
    @api.response(404, 'Not found')
    def get(self, manager_id):
        ''' Retrieves a list of associates for a designated manager id '''
        associates = assoc_db.read_all_associates_by_query({'manager_id': manager_id})
        to_return = []
        for associate in associates:
            swots = []
            if associate['swot']:
                for swot in associate['swot']:
                    swot['date_created'] = converter(swot['date_created'])
                    swots.append(swot)
            else:
                associate['swot'] = [{'author': 'trainer'}]
            data = {'name': associate['name'], 'SWOT': swots, 'ID': associate['email'],
                    'status': associate['status']}
            to_return.append(data)
        if len(associates) == 0:
            return [], 404
        else:
            return to_return, 200

@api.route('/employees/<str:user_id>')
class EmployeeIdRoute(Resource):
    '''Class for routing employee/user_id requests'''
    @api.response(200, 'Success', associate_model)
    @api.response(404, 'Not found')
    def get(self, user_id):
        ''' Retrieves associate information for a designated
        associate vai salesforce id or email '''
        if 'SF' in user_id: # Query with salesforce ID if that was the request
            res = assoc_db.read_one_associate_by_query({'salesforce_id': user_id})
        else: # Assume it it is an email otherwise
            res = assoc_db.read_one_associate_by_query({'email': user_id})
        if res['swot']:
            for swot in res['swot']:
                swot['date_created'] = converter(swot['date_created'])
        else:
            res['swot'] = [{'author': 'trainer'}]
        res.pop('_id')
        res['end_date'] = converter(res['end_date'])
        if res:
            return res, 200
        else:
            return {}, 404

    @api.doc(body=swot_fields)
    @api.response(201, 'Item Created', swot_fields)
    @api.response(400, 'Invalid request')
    def post(self, user_id):
        ''' Adds a SWOT to a designated associate via their salesforce id or email '''
        if 'SF' in user_id:
            res = swot_db.create_swot('salesforce_id', user_id, flask.request.get_json(force=True))
        else:
            res = swot_db.create_swot('email', user_id, flask.request.get_json(force=True))
        if type(res) == str:
            return res, 400
        else:
            return res, 201

@api.route('/employees/<str:user_id>/evaluations')
class EmployeeIdEvaluationsRoute(Resource):
    '''Class for routing employee/user_id/evaluations requests'''
    @api.response(200, 'Success', associate_evaluation_model)
    @api.response(404, 'Not found')
    def get(self, user_id):
        ''' Retrieves evaluations for a designated associate via email address '''
        query = {'email': user_id}
        batch_id = assoc_db.get_associate_batch_id(query)
        sf_id = assoc_db.get_associate_sf_id(user_id)
        if sf_id:
            qc_data = get_qc_data(sf_id)
        if batch_id:
            batch_spider_data, associate_spider_data = get_batch_and_associate_spider_data(user_id, batch_id)
        else:
            return {}, 404
        return {'batch_spider': batch_spider_data, 'associate_spider': associate_spider_data,
                'qc': qc_data}, 200
            

