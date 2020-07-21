''' Handles manager routes. Only login for now '''

from flask_restplus import Resource, Api
from src.data.data import _db

api = Api()

@api.route('/managers/<str:manager_id>')
@api.doc()
class BatchRoute(Resource):
    '''Class for routing batch requests'''
    @api.response(200, 'Test success')
    def get(self, manager_id):
        '''Function for handling GET /manager requests'''
        return _db.manager_login(manager_id)
        
