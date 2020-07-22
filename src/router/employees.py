''' Handles employee routes  '''
import json
import flask

from flask_restplus import Resource, Api, fields, Model
import src.data.associates_db as assoc_db
import src.data.swot_db as swot_db
from src.external.caliber_processing import get_qc_data, get_spider_data
from src.data.date_time_conversion import converter

from src.models.swot import SWOT

from src.logging.logger import get_logger

_log = get_logger(__name__)

api = Api()

''' SWOT Item model for documentation and validation '''
swot_item = Model('SWOT Item', {
    'category': fields.String,
    'notes': fields.String
})

''' SWOT model for documentation and validation '''
swot_fields = Model('SWOT', {
    'strengths': fields.List(fields.Nested(swot_item)),
    'weaknesses': fields.List(fields.Nested(swot_item)),
    'opportunities': fields.List(fields.Nested(swot_item)),
    'threats': fields.List(fields.Nested(swot_item)),
    'notes': fields.String,
    'creationDate': fields.DateTime
})


@api.route('/employees')
@api.doc()
class EmployeeRoute(Resource):
    '''Class for routing employee requests'''
    @api.response(200, 'Success')
    def get(self):
        '''Function for handling GET /employees requests'''
        emp_lst = list(assoc_db.read_all_associates())
        for i in range(0, len(emp_lst) - 1):
            if emp_lst[i]['_id'] == 'UNIQUE_COUNT':
                del emp_lst[i]
            emp_lst[i].pop('_id')
            emp_lst[i]['end_date'] = converter(emp_lst[i]['end_date'])
        _log.debug(emp_lst)
        return json.dumps(emp_lst)

@api.route('/employees/manager/<str:manager_id>')
@api.doc()
class EmployeeManagerRoute(Resource):
    '''Class for routing employee/manager/manager_id requests'''
    @api.response(200, 'Success')
    def get(self, manager_id):
        '''Function for handling GET /employees/manager/manager_id requests'''
        return {'status': "yippee"}

@api.route('/employees/<str:user_id>')
@api.doc()
class EmployeeIdRoute(Resource):
    '''Class for routing employee/user_id requests'''
    @api.response(200, 'Success')
    def get(self, user_id):
        '''Function for handling GET /employees/user_id requests'''
        if 'SF' in user_id: # Query with salesforce ID if that was the request
            res = assoc_db.read_one_associate_by_query({'salesforce_id': user_id})
        else: # Assume it it is an email otherwise
            res = assoc_db.read_one_associate_by_query({'email': user_id})
        if res and 'swot' in res: # Replace the ID of the swot with the swot itself in response
            for ind, swot in enumerate(res['swot']):
                this_swot = SWOT.from_dict(swot_db.read_swot_by_id(res['swot'][ind]))
                res['swot'][ind] = this_swot.to_dict()

        return res

    @api.doc(body=swot_fields)
    @api.response(200, 'Status code of response')
    def post(self, user_id):
        '''Function for handling PUT /employees/user_id requests'''
        if 'SF' in user_id:
            res = swot_db.create_swot('salesforce_id', user_id, flask.request.get_json(force=True))
        else:
            res = swot_db.create_swot('email', user_id, flask.request.get_json(force=True))
        return res

@api.route('/employees/<str:user_id>/evaluations')
@api.doc()
class EmployeeIdEvaluationsRoute(Resource):
    '''Class for routing employee/user_id/evaluations requests'''
    @api.response(200, 'Success')
    def get(self, user_id):
        '''Function for handling GET /employees/user_id/evaluations requests'''
        sf_id = assoc_db.get_associate_sf_id(user_id)
        qc_data = get_qc_data(sf_id)
        spider_data = get_spider_data(user_id)
        return {'spider': spider_data, 'qc': qc_data}
