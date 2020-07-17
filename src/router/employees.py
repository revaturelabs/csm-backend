''' Handles employee routes  '''
import json
from flask_restplus import Resource, Api, fields
import src.data.data as db
import src.external.evaluation_service as evaluate
from src.testing_logging.logger import get_logger

_log = get_logger(__name__)

api = Api()

swot_fields = Model('SWOT', {
    'strengths': fields.List(fields.String),
    'weaknesses': fields.List(fields.String),
    'opportunities': fields.List(fields.String),
    'threats': fields.List(fields.String),
    'notes': fields.String
})

@api.route('/employees')
@api.doc()
class EmployeeRoute(Resource):

    @api.response(200, 'Success')
    def get(self):
        return {'status': "yippee"}

@api.route('/employees/manager/<str:manager_id>')
@api.doc()
class EmployeeManagerRoute(Resource):

    @api.response(200, 'Success')
    def get(self, manager_id):
        return {'status': "yippee"}

@api.route('/employees/<str:user_id>')
@api.doc()
class EmployeeIdRoute(Resource):

    @api.response(200, 'Success')
    def get(self):
        return {'status': "yippee"}

    @api.doc(body=swot_fields)
    @api.response(204, 'No Content')
    def put(self, user_id):
        return 'No content'

@api.route('/employees/<str:batch_id>/evaluations/<str:user_id>')
@api.doc()
class EmployeeIdEvaluationsRoute(Resource):

    @api.response(200, 'Success')
<<<<<<< HEAD
    def get(self, user_id):
        return {'status': "yippee"}
=======
    def get(self, batch_id, user_id):
        spider_data = evaluate.get_associate_spider_data(batch_id, user_id)
        spider_data = json.loads(spider_data)
        for data_dict in spider_data:
            data_dict.pop('traineeId')
            data_dict.pop('weight')
        _log.debug(type(spider_data))
        return spider_data, 200
>>>>>>> 59572580da2d90c475a2b357594d5a89e2ced0a1
