''' Handles employee routes  '''

from flask_restplus import Resource, Api, fields, Model
import src.data as db

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

@api.route('/employees/<str:user_id>/evaluations')
@api.doc()
class EmployeeIdEvaluationsRoute(Resource):

    @api.response(200, 'Success')
    def get(self, user_id):
        return {'status': "yippee"}
