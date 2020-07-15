''' Handles employee routes  '''

from flask_restplus import Resource, Api, fields
import src.data as db

api = Api()

swot_fields = api.model('SWOT', {
    'Strengths': fields.String,
    'Weaknesses': fields.String,
    'Opportunities': fields.String,
    'Threats': fields.String,
    'Notes': fields.String
})

@api.route('/employees')
@api.doc()
class EmployeeRoute(Resource):

    @api.response(200, 'Test success')
    def get(self):
        return {'status': "yippee"}

@api.route('/employees/manager/<str:manager_id>')
@api.doc()
class EmployeeManagerRoute(Resource):

    @api.response(200, 'Test success')
    def get(self):
        return {'status': "yippee"}

@api.route('/employees/<str:user_id>')
@api.doc()
class EmployeeIdRoute(Resource):

    @api.response(200, 'Success')
    def get(self):
        return {'status': "yippee"}

    @api.expect(body=swot_fields)
    @api.response(204)
    def put(self, new_swot):
        return {'status': "yippee"}

@api.route('/employees/<str:user_id>/evaluations')
@api.doc()
class EmployeeIdEvaluationsRoute(Resource):

    @api.response(200, 'Success')
    def get(self):
        return {'status': "yippee"}
