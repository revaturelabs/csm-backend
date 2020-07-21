''' Handles employee routes  '''
import json
import flask
from flask_restplus import Resource, Api, fields, Model
import src.data.associates_db as assoc_db
import src.data.swot_db as swot_db
import src.external.evaluation_service as evaluate

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
        return {'status': "yippee"}

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
        if 'SF' in user_id:
            res = assoc_db.read_one_associate_by_query({'salesforce_id': user_id})
        else:
            res = assoc_db.read_one_associate_by_query({'email': user_id})
        return res

    @api.doc(body=swot_fields)
    @api.response(200, 'Status code of response')
    def put(self, user_id):
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
        query = {'email': user_id}
        batch_id = assoc_db.get_associate_batch_id(query)
        spider_data = evaluate.get_associate_spider_data(batch_id, user_id)
        spider_data = json.loads(spider_data)
        for data_dict in spider_data:
            data_dict.pop('traineeId')
            data_dict.pop('weight')
        _log.debug(type(spider_data))
        return spider_data
